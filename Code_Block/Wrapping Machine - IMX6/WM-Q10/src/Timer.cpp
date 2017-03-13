#include "../include/common.h"

/* ------------------------------------------------------------------------- */
#define DEF_WINTIMER_RATE   1  /* ms */

/* ------------------------------------------------------------------------- */
extern HWND hMainWnd ;
extern HWND hRunDlgWnd ;
extern int  iMainNeedScan ;
extern int  ubRS232IsExist ;
extern int  iTestSavefile ;
/* ------------------------------------------------------------------------- */
extern long ulRS232_Read( unsigned char *ubData , long ulBytes ) ;
extern void vRS232_Write( unsigned char *ubData , long ulBytes ) ;

extern void vConsole_Add( const char *cStr , int iLength ) ;
extern void vConsole_Save( const char *cStr , int iLength ) ;
extern void vConsole_Show( HWND hWnd ) ;

/* ------------------------------------------------------------------------- */
UINT uiTimerID = 0 ;
int iTimerCount = 0 ;
int iRebootStart = 0 ;
/* ------------------------------------------------------------------------- */
void CALLBACK vTimer_Process( UINT uID , UINT uMsg , DWORD dwUser , DWORD dw1 , DWORD dw2 )
{
    unsigned char ubBuf[2048] ;
    long ulBytes ;

    if ( iMainNeedScan )
    {
        SendMessage( hMainWnd , WM_USER1 , 0 , 0 ) ;
    }

    if ( ubRS232IsExist )
    {
        ulBytes = ulRS232_Read( ubBuf , 1024 ) ;
        if ( ulBytes )
        {
            if ( iTestSavefile )
                vConsole_Save( (const char *)ubBuf , ulBytes ) ;
            vConsole_Add( (const char *)ubBuf , ulBytes ) ;
            vConsole_Show( hRunDlgWnd ) ;
            //SetDlgItemText( hMainWnd , IDC_EDIT_CONSOLE , (LPCSTR)ubBuf ) ;
        }
    }

    if ( hMainWnd )
    {
        SendMessage( hMainWnd , WM_USER2 , 0 , 0 ) ;
    }

    if ( iRebootStart ){
        char cTemp[32] ;
        iTimerCount ++ ;
        sprintf(cTemp,"%d",iTimerCount/1000) ;
        vTimer_Show( cTemp ) ;
    }

}

BOOL bTimer_Start( HWND mHwnd )
{
    TIMECAPS        stcCaps ;

    timeGetDevCaps( &stcCaps, sizeof(stcCaps) ) ;
    timeBeginPeriod( stcCaps.wPeriodMin ) ;
    uiTimerID = timeSetEvent( DEF_WINTIMER_RATE / stcCaps.wPeriodMin ,
                                stcCaps.wPeriodMin ,
                                (LPTIMECALLBACK)vTimer_Process ,
                                (DWORD)0 ,
                                TIME_PERIODIC
                              ) ;
    if( !uiTimerID )
    {
        return ( FALSE ) ;
    }

    return ( TRUE ) ;
}

void vTimer_Stop( HWND mHwnd )
{
    TIMECAPS        stcCaps ;

    if( uiTimerID )
    {
        timeKillEvent( uiTimerID ) ;
        timeGetDevCaps( &stcCaps , sizeof(stcCaps) ) ;
        timeEndPeriod( stcCaps.wPeriodMin ) ;
        uiTimerID = 0 ;
    }
}

