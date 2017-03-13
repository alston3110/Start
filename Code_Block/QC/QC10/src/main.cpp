#include "../include/common.h"

/* ------------------------------------------------------------------------- */
HINSTANCE hMainInst ;
HWND      hMainWnd = NULL ;
int       iMainRS232StartOrStop = 0 ;
int       iMainNeedScan = 0 ;
int       iMainPortNum = 0 ;

/* ------------------------------------------------------------------------- */
extern int iRS232_ListPorts( HWND hComboWnd ) ;
extern BOOL bTimer_Start( HWND mHwnd ) ;
extern void vTimer_Stop( HWND mHwnd ) ;
extern void vRS232_Start( const char *cPort ) ;
extern void vRS232_Close( void ) ;
extern void vConsole_Init( void ) ;
extern void vConsole_Debug( void ) ;
extern void vReport_Init( HWND hWnd ) ;
extern void vTest_Process( void ) ;

extern int iTestReturnBool ;
/* ------------------------------------------------------------------------- */
BOOL CALLBACK DlgMain(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch(uMsg)
    {
        case WM_INITDIALOG:
            {
                HWND hComboWnd  = GetDlgItem( hwndDlg , IDC_COMBO_PORT ) ;

                ShowWindow(GetDlgItem(hwndDlg, IDC_BUTTON_YES_NO_OK), SW_HIDE);
                ShowWindow(GetDlgItem(hwndDlg, IDC_BUTTON_YES_NO_FAIL), SW_HIDE);
                ShowWindow(GetDlgItem(hwndDlg, IDC_BUTTON_RESTART), SW_HIDE);

                hMainWnd = hwndDlg ;
                vConsole_Init( ) ;

                if ( iRS232_ListPorts( hComboWnd ) )
                {
                    SendMessage( hComboWnd , CB_SETCURSEL , 0 , 0 ) ;
                }
                iMainPortNum = SendMessage( hComboWnd , CB_GETCOUNT , 0 , 0 ) ;
                /*
                {
                    char cTempStr[256] ;
                    sprintf( cTempStr , "%08X" , _WIN32_IE ) ;
                    MessageBox( NULL , cTempStr , NULL , NULL ) ;
                }
                */
                if ( iMainPortNum )
                {
                    iMainNeedScan = 0 ;
                }
                else
                {
                    iMainNeedScan = 1 ;
                }
                Button_Enable( GetDlgItem( hwndDlg , IDC_BUTTON_START ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_INPUT ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_INPUT1 ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_INPUT2 ) , FALSE ) ;
                vReport_Init( GetDlgItem( hwndDlg , IDC_LIST_REPORT ) ) ;
                Edit_Enable( GetDlgItem( hMainWnd , IDC_EDIT_NO ) , FALSE ) ;

                SendMessage( GetDlgItem( hwndDlg , IDC_PROGRESS_WAIT ) , PBM_SETRANGE , 0 , MAKELPARAM( 0 , 1000 ) ) ;

                bTimer_Start( hwndDlg ) ;

            }
            return ( TRUE ) ;

        case WM_CLOSE:
            vTimer_Stop( hwndDlg ) ;
            EndDialog( hwndDlg , 0 ) ;
            return ( TRUE ) ;

        case WM_COMMAND:
            switch(LOWORD(wParam))
            {
                case IDC_BUTTON_START :
                    {
                        HWND hButtonWnd = GetDlgItem( hwndDlg , IDC_BUTTON_START ) ;
                        //HWND hScanButtonWnd = GetDlgItem( hwndDlg , IDC_BUTTON_RS232_SCAN ) ;
                        //HWND hInputWnd = GetDlgItem( hwndDlg , IDC_EDIT_INPUT ) ;
                        //HWND hInputInfoWnd = GetDlgItem( hwndDlg , IDC_STATIC_INPUT ) ;

                        if ( iMainRS232StartOrStop == 0 )
                        {
                            char cPort[16] ;
                            TCHAR szTempStr[32] ;

                            GetDlgItemText( hwndDlg , IDC_COMBO_PORT , cPort , 9 ) ;
                            LoadString( hMainInst , IDS_STRING_STOP , szTempStr , 32 ) ;
                            SendMessage( hButtonWnd , WM_SETTEXT , 0 , (LPARAM)szTempStr ) ;
                            vRS232_Start( cPort ) ;
                            iMainRS232StartOrStop = 1 ;
                            //SetFocus( hInputWnd ) ;
                            //SendMessage( hInputInfoWnd , WM_SETTEXT , 0 , (LPARAM) "8code" ) ;
                            //Button_Enable( hScanButtonWnd , FALSE ) ;
                        }
                        else
                        {
                            TCHAR szTempStr[32] ;

                            LoadString( hMainInst , IDS_STRING_START , szTempStr , 32 ) ;
                            SendMessage( hButtonWnd , WM_SETTEXT , 0 , (LPARAM)szTempStr ) ;

                            vRS232_Close( ) ;
                            iMainRS232StartOrStop = 0 ;
                            //SendMessage( hInputInfoWnd , WM_SETTEXT , 0 , (LPARAM) "None" ) ;
                            //Button_Enable( hScanButtonWnd , TRUE ) ;
                        }
                    }
                    return ( TRUE ) ;
                case IDC_BUTTON_RS232_SCAN :
                    {
                        HWND hComboWnd = GetDlgItem( hwndDlg , IDC_COMBO_PORT ) ;
                        HWND hButtonWnd = GetDlgItem( hwndDlg , IDC_BUTTON_START ) ;

                        vRS232_Close( ) ;
                        iMainPortNum = SendMessage( hComboWnd , CB_GETCOUNT , 0 , 0 ) ;
                        if ( iMainPortNum )
                        {
                            SendMessage( hComboWnd , CB_RESETCONTENT , 0 , 0 ) ;
                        }
                        if ( iRS232_ListPorts( hComboWnd ) )
                        {
                            SendMessage( hComboWnd , CB_SETCURSEL , 0 , 0 ) ;
                        }
                        iMainPortNum = SendMessage( hComboWnd , CB_GETCOUNT , 0 , 0 ) ;
                        if ( iMainPortNum )
                        {
                            iMainNeedScan = 0 ;
                        }
                        else
                        {
                            iMainNeedScan = 1 ;
                        }
                    }
                    return ( TRUE ) ;
                case IDC_BUTTON_YES_NO_FAIL :
                    iTestReturnBool = 1 ;
                    return ( TRUE ) ;
                case IDC_BUTTON_YES_NO_OK :
                    iTestReturnBool = 2 ;
                    return ( TRUE ) ;
                case IDC_BUTTON_RESTART :
                    iTestReturnBool = 3 ;
                    return ( TRUE ) ;
            }
            return ( TRUE ) ;
        case WM_USER1 :
            {
                /*重新掃描 com port , 並加入 List 中*/
                HWND hComboWnd = GetDlgItem( hwndDlg , IDC_COMBO_PORT ) ;
                HWND hButtonWnd = GetDlgItem( hwndDlg , IDC_BUTTON_START ) ;

                iMainPortNum = SendMessage( hComboWnd , CB_GETCOUNT , 0 , 0 ) ;
                if ( iMainPortNum )
                {
                    SendMessage( hComboWnd , CB_RESETCONTENT , 0 , 0 ) ;
                    //MessageBox( NULL , "test" , NULL , NULL ) ;
                }
                if ( iRS232_ListPorts( hComboWnd ) )
                {
                    SendMessage( hComboWnd , CB_SETCURSEL , 0 , 0 ) ;
                }
                iMainPortNum = SendMessage( hComboWnd , CB_GETCOUNT , 0 , 0 ) ;

                if ( iMainRS232StartOrStop )
                {
                    TCHAR szTempStr[32] ;
                    /* 設定 "開始" 字樣*/
                    LoadString( hMainInst , IDS_STRING_START , szTempStr , 32 ) ;
                    //MessageBox( NULL , cTempStr , NULL , NULL ) ;
                    SendMessage( hButtonWnd , WM_SETTEXT , 0 , (LPARAM)szTempStr ) ;
                    iMainRS232StartOrStop = 0 ;
                    Button_Enable( hButtonWnd , FALSE ) ;
                }

                if ( iMainPortNum )
                {
                    iMainNeedScan = 0 ;
                }
                else
                {
                    iMainNeedScan = 1 ;
                }
            }
            return ( TRUE ) ;
        case WM_USER2 :
            vTest_Process( ) ;
            return ( TRUE ) ;
    }
    return ( FALSE ) ;
}


int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
{
#if 0
    HWND hDlg ;
    MSG  uMsg ;
    BOOL bRet ;
#endif

    hMainInst = hInstance ;
    InitCommonControls( ) ;
#if 0
    hDlg = CreateDialogParam( hMainInst , MAKEINTRESOURCE(DLG_MAIN) , 0 , DlgMain , 0 ) ;
    ShowWindow( hDlg, nShowCmd ) ;

    while( ( bRet = GetMessage( &uMsg , 0 , 0 , 0 ) ) != 0 )
    {
        if( bRet == -1 )
        {
            return -1;
        }

        if( !IsDialogMessage( hDlg , &uMsg ) )
        {
            TranslateMessage(&uMsg);
            DispatchMessage(&uMsg);
        }
  }
#endif

    return DialogBox( hMainInst , MAKEINTRESOURCE(DLG_MAIN) , NULL , (DLGPROC)DlgMain ) ;
}
