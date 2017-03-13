#include "../include/common.h"

extern int iRS232_ListPorts( HWND hComboWnd ) ;
extern void vRS232_Close( void ) ;

extern int       iMainNeedScan ;
extern int       iMainPortNum ;

HWND hSettingDlgWnd = NULL ;
/* ------------------------------------------------------------------------- */

BOOL CALLBACK bSettingDlg_Main(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch(uMsg)
    {
        case WM_INITDIALOG:
            {
                HWND hComboWnd  = GetDlgItem( hwndDlg , IDC_COMBO_PORT ) ;
                hSettingDlgWnd = hwndDlg ;

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

        case WM_CLOSE:
            EndDialog( hwndDlg , 0 ) ;
            return ( TRUE ) ;

        case WM_COMMAND:
            switch(LOWORD(wParam))
            {
                case IDC_BUTTON_RS232_SCAN :
                    {
                        HWND hComboWnd = GetDlgItem( hwndDlg , IDC_COMBO_PORT ) ;

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
            }
            return ( TRUE ) ;
    }
    return ( FALSE ) ;
}
