#include "../include/common.h"

/* ------------------------------------------------------------------------- */
extern HINSTANCE hMainInst ;
extern HWND      hMainWnd  ;

/* ------------------------------------------------------------------------- */
HWND hWaitPCBWnd = NULL ;
int  iWaitPCBCount = 0 ;
UINT uiWaitPCBTimerID = 0 ;

/* ------------------------------------------------------------------------- */

void CALLBACK vWaitPCB_TimerProcess( UINT uID , UINT uMsg , DWORD dwUser , DWORD dw1 , DWORD dw2 )
{
    if ( hWaitPCBWnd )
    {
        SendMessage( hWaitPCBWnd , WM_USER2 , 0 , 0 ) ;
        //vStatus_Show( "Sent USER2" ) ;
        MessageBox( NULL , "test" , NULL , NULL ) ;
    }
}

BOOL bWaitPCB_TimerStart( HWND mHwnd )
{
    TIMECAPS        stcCaps ;

    timeGetDevCaps( &stcCaps, sizeof(stcCaps) ) ;
    timeBeginPeriod( stcCaps.wPeriodMin ) ;

    // 1 ms
    uiWaitPCBTimerID = timeSetEvent( 1 / stcCaps.wPeriodMin ,
                                stcCaps.wPeriodMin ,
                                (LPTIMECALLBACK)vWaitPCB_TimerProcess ,
                                (DWORD)0 ,
                                TIME_PERIODIC
                              ) ;
    if( !uiWaitPCBTimerID )
    {
        return ( FALSE ) ;
    }
    MessageBox( NULL , "1111" , NULL , NULL ) ;
    return ( TRUE ) ;
}

void vWaitPCB_TimerStop( HWND mHwnd )
{
    TIMECAPS        stcCaps ;

    if( uiWaitPCBTimerID )
    {
        timeKillEvent( uiWaitPCBTimerID ) ;
        timeGetDevCaps( &stcCaps , sizeof(stcCaps) ) ;
        timeEndPeriod( stcCaps.wPeriodMin ) ;
        uiWaitPCBTimerID = 0 ;
    }
}

BOOL CALLBACK cbWaitPCB_MsgProc(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch(uMsg)
    {
        case WM_INITDIALOG:
            {
                HWND hWnd = GetDlgItem( hwndDlg , IDC_PROGRESS_WAIT_PCBA ) ;

                hWaitPCBWnd   = hwndDlg ;
                iWaitPCBCount = 0 ;
                SendMessage( hWnd , PBM_SETRANGE , 0 , MAKELPARAM( 0 , 220 ) ) ;
                bWaitPCB_TimerStart( hwndDlg ) ;
            }
            return ( TRUE ) ;

        case WM_CLOSE:
            vWaitPCB_TimerStop( hwndDlg ) ;
            EndDialog( hwndDlg , 0 ) ;
            hWaitPCBWnd = NULL ;
            return ( TRUE ) ;

        case WM_COMMAND:
            switch(LOWORD(wParam))
            {

            }
            return ( TRUE ) ;
        case WM_USER2 :
            {
                HWND hWnd = GetDlgItem( hwndDlg , IDC_PROGRESS_WAIT_PCBA ) ;
                MessageBox( NULL , "test" , NULL , NULL ) ;
                iWaitPCBCount ++ ;
                SendMessage(hWnd , PBM_SETPOS, iWaitPCBCount, 0);

            }
            return ( TRUE ) ;
    }
    return ( FALSE ) ;
}

int iWaitPCB_Run( void )
{
    DialogBox( NULL , MAKEINTRESOURCE(IDD_DIALOG_WAIT_PCB) , NULL , (DLGPROC)cbWaitPCB_MsgProc ) ;
}
