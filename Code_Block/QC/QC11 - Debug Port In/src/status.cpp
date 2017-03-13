#include "../include/common.h"

/* ------------------------------------------------------------------------- */
extern HWND      hMainWnd ;

/* ------------------------------------------------------------------------- */
void vStatus_Show( const char *cStr )
{
    if ( cStr )
    {
        HWND hWnd  = GetDlgItem( hMainWnd , IDC_STATIC_STATE ) ;

        SetWindowText( hWnd , cStr ) ;
        //SendMessage( hWnd , WM_SETTEXT , 0 , (LPARAM) cStr ) ;
    }
}

