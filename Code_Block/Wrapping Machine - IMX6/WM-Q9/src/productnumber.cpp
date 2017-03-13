#include "../include/common.h"

/* ------------------------------------------------------------------------- */
FAR WNDPROC pProductNumberWndProc ;

/* ------------------------------------------------------------------------- */
LRESULT CALLBACK cbProductNumber_CallBackProc( HWND hDlg , UINT uMsg , WPARAM wParam , LPARAM lParam )
{
    switch( uMsg )
    {
        case WM_CHAR:
            if( wParam == 13 )
            {
                //MessageBox( NULL , "test" , NULL , NULL ) ;
                /* User pressed ENTER -- do what you want here. */
                return(0);
            }
            break;
    }
    return( (LRESULT)CallWindowProc( (WNDPROC)pProductNumberWndProc , hDlg , uMsg , wParam , lParam ) );
}

void vProductNumber_Init( HWND hWnd )
{
    pProductNumberWndProc = (WNDPROC)GetWindowLong( hWnd , GWL_WNDPROC ) ;
    SetWindowLong( hWnd , GWL_WNDPROC , (long)cbProductNumber_CallBackProc ) ;
}
