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

extern void vTest_Process( void ) ;

extern void vMainTab_Init( HWND hwnd ) ;
extern void vMainTab_Select( HWND hwnd , LPNMHDR nmptr ) ;
extern void vMainTab_Close( void ) ;

extern HWND hSettingDlgWnd ;
extern HWND hRunDlgWnd ;

/* ------------------------------------------------------------------------- */
BOOL CALLBACK DlgMain(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch(uMsg)
    {
        case WM_INITDIALOG:
            {
                vMainTab_Init( hwndDlg ) ;
                hMainWnd = hwndDlg ;
                SetWindowText( GetDlgItem( hSettingDlgWnd , USER_NAME ) , "root" ) ;
                SetWindowText( GetDlgItem( hSettingDlgWnd , PASSWORD ) , "" ) ;
                SetWindowText( GetDlgItem( hSettingDlgWnd , MP_PATH ) , "/mnt/mmcblk1p1/MP_TEST/MP_Test" ) ;
                bTimer_Start( hwndDlg ) ;
            }
            return ( TRUE ) ;

        case WM_CLOSE:
            vTimer_Stop( hwndDlg ) ;
            vMainTab_Close( ) ;
            EndDialog( hwndDlg , 0 ) ;
            return ( TRUE ) ;
		case WM_NOTIFY :
			vMainTab_Select( hwndDlg , (LPNMHDR)lParam ) ;
			return ( TRUE ) ;
        case WM_COMMAND:
            return ( TRUE ) ;
        case WM_USER1 :
            {
                /*重新掃描 com port , 並加入 List 中*/
                if ( (hSettingDlgWnd == NULL) || (hRunDlgWnd == NULL) )
                {
                    return ( TRUE ) ;
                }
                HWND hComboWnd = GetDlgItem( hSettingDlgWnd , IDC_COMBO_PORT ) ;
                HWND hButtonWnd = GetDlgItem( hRunDlgWnd , IDC_BUTTON_START ) ;

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
