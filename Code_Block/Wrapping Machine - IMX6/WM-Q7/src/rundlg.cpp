#include "../include/common.h"

extern void vConsole_Init( void ) ;
extern void vReport_Init( HWND hWnd ) ;
extern void vRS232_Start( const char *cPort ) ;
extern void vRS232_Close( void ) ;

extern HINSTANCE hMainInst ;
extern int iMainRS232StartOrStop ;
extern HWND hSettingDlgWnd ;
extern int iTestReturnBool ;

HWND hRunDlgWnd = NULL ;

/* ------------------------------------------------------------------------- */
#if 0
LRESULT lRunDlg_OnNotify( LPARAM lParam )
{
    NMHDR* pnmh = (NMHDR*) lParam ;
    LV_DISPINFO* pdi ;

    switch(pnmh->code)
    {
        case NM_CUSTOMDRAW:
            {
                LPNMLVCUSTOMDRAW lpNMCustomDraw = (LPNMLVCUSTOMDRAW) lParam;
                switch( lpNMCustomDraw->nmcd.dwDrawStage )
                {
                    case CDDS_PREPAINT :
                        //SetWindowLong(hRunDlgWnd,DWL_MSGRESULT,CDRF_NOTIFYITEMDRAW); // Comment this line out if this is not a dialog obx
                        return CDRF_NOTIFYITEMDRAW;

                    case CDDS_ITEMPREPAINT:
                        if (((int)lpNMCustomDraw->nmcd.dwItemSpec%2)==0)
                        {
                            //customize item appearance
                            lpNMCustomDraw->clrText   = RGB(255,0,0);
                            lpNMCustomDraw->clrTextBk = RGB(200,200,200);
                            return CDRF_NEWFONT;
                        }
                        else{
                            lpNMCustomDraw->clrText   = RGB(0,0,255);
                            lpNMCustomDraw->clrTextBk = RGB(255,255,255);
                            return CDRF_NEWFONT;
                        }

                        break;
                }
            }
            return CDRF_DODEFAULT;
            //MessageBox( NULL , "test" , NULL , NULL ) ;
            break ;
    }
    return 0;
}
#endif

BOOL CALLBACK bRunDlg_Main(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch(uMsg)
    {
        case WM_INITDIALOG:
            {
                hRunDlgWnd = hwndDlg ;
                ShowWindow(GetDlgItem(hwndDlg, IDC_BUTTON_YES_NO_OK), SW_HIDE);
                ShowWindow(GetDlgItem(hwndDlg, IDC_BUTTON_YES_NO_FAIL), SW_HIDE);
                ShowWindow(GetDlgItem(hwndDlg, IDC_BUTTON_RESTART), SW_HIDE);
                Button_Enable( GetDlgItem( hwndDlg , IDC_BUTTON_START ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_INPUT ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_INPUT1 ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_INPUT2 ) , FALSE ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT1 ) , FALSE ) ;
                vReport_Init( GetDlgItem( hwndDlg , IDC_LIST_REPORT ) ) ;
                Edit_Enable( GetDlgItem( hwndDlg , IDC_EDIT_NO ) , FALSE ) ;

                vConsole_Init( ) ;
            }
            return ( TRUE ) ;

        case WM_CLOSE:
            EndDialog( hwndDlg , 0 ) ;
            return ( TRUE ) ;
		//case WM_NOTIFY :
		    //lRunDlg_OnNotify( (LPARAM)lParam ) ;
            //MessageBox( NULL , "ttttt" , NULL , NULL ) ;
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

                            GetDlgItemText( hSettingDlgWnd , IDC_COMBO_PORT , cPort , 9 ) ;
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
    }
    return ( FALSE ) ;
}
