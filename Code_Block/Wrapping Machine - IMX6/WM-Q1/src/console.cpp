#include "../include/common.h"

/* ------------------------------------------------------------------------- */
extern void vTest_Check( unsigned char ubCh ) ;

/* ------------------------------------------------------------------------- */
#define DEF_CONSOLE_MAX_CHAR 1024
#define DEF_CONSOLE_MAX_LINE 256

/* ------------------------------------------------------------------------- */
typedef struct __CONSOLE_LINE__ {
    char  cData[DEF_CONSOLE_MAX_CHAR] ;
    int   iLen ;
    int   iStart ;
} CONSOLE_LINE ;

/* ------------------------------------------------------------------------- */
CONSOLE_LINE stcConsoleLineRoot[DEF_CONSOLE_MAX_LINE] ;

int iConsoleLoop  = 0 ;
int iConsoleEnd   = 0 ;

/* ------------------------------------------------------------------------- */
void vConsole_Init( void )
{
    memset( (void *)&stcConsoleLineRoot[0] , 0 , sizeof(CONSOLE_LINE) * DEF_CONSOLE_MAX_LINE ) ;
    iConsoleLoop  = 0 ;
    iConsoleEnd   = 0 ;

    {
        FILE *ofp ;
        ofp = fopen( "consoledebug.txt" , "wb" ) ;
        if ( ofp )
        {
            fprintf( ofp , "*****start*****\r\n" ) ;
            fclose( ofp ) ;
        }
    }

}

void vConsole_Add( const char *cStr , int iLength )
{
    int iLoop ;
    CONSOLE_LINE *pLine ;

    if ( iLength )
    {

        {
            FILE *ofp ;

            ofp = fopen( "consoledebug.txt" , "a+" ) ;
            if ( ofp )
            {
                fwrite( cStr , 1 , iLength , ofp );
                fclose( ofp ) ;
            }
        }
        pLine = &stcConsoleLineRoot[iConsoleEnd] ;
        for ( iLoop = 0 ; iLoop < DEF_CONSOLE_MAX_CHAR ; iLoop ++ )
        {
            if ( iLoop >= iLength )
            {
                break ;
            }

            vTest_Check( cStr[iLoop] ) ;

            switch ( cStr[iLoop] )
            {
                case 0x0A :
                    iConsoleEnd ++ ;
                    if ( iConsoleEnd >= DEF_CONSOLE_MAX_LINE )
                    {
                        iConsoleEnd  = 0 ;
                        iConsoleLoop = 1 ;
                    }
                    pLine = &stcConsoleLineRoot[iConsoleEnd] ;
                    pLine->iStart = 0 ;
                    pLine->iLen   = 0 ;
                    break ;
                case 0x0D :
                    pLine->iLen = 0 ;
                    break ;
                default :
                    if ( pLine->iLen < DEF_CONSOLE_MAX_CHAR - 1 )
                    {
                        pLine->cData[pLine->iLen] = cStr[iLoop] ;
                        pLine->cData[pLine->iLen+1] = 0 ;
                        pLine->iLen ++ ;
                    }
                    break ;
            }
        }
    }
}

void vConsole_Show( HWND hWnd )
{
    char *cBuf ;
    int iLoop ;
    int iLines ;

    cBuf = (char *)malloc(DEF_CONSOLE_MAX_CHAR*DEF_CONSOLE_MAX_LINE) ;
    cBuf[0] = 0 ;
    if ( cBuf )
    {
        HWND hEditWnd = GetDlgItem( hWnd , IDC_EDIT_CONSOLE ) ;

        if ( iConsoleLoop )
        {
            if ( iConsoleEnd < DEF_CONSOLE_MAX_LINE-1 )
            {
                for ( iLoop = iConsoleEnd+1 ; iLoop < DEF_CONSOLE_MAX_LINE ; iLoop ++ )
                {
                    strcat( cBuf , stcConsoleLineRoot[iLoop].cData ) ;
                    strcat( cBuf , "\r\n" ) ;
                }
            }
        }
        for ( iLoop = 0 ; iLoop < iConsoleEnd ; iLoop ++ )
        {
            strcat( cBuf , stcConsoleLineRoot[iLoop].cData ) ;
            strcat( cBuf , "\r\n" ) ;
        }
        //SetDlgItemText( hWnd , IDC_EDIT_CONSOLE , (LPCSTR)cBuf ) ;
        Edit_SetText( hEditWnd , (LPCSTR)cBuf ) ;
        iLines = SendMessage( hEditWnd , EM_GETLINECOUNT , (WPARAM)0 , (LPARAM)0 ) ;
        Edit_Scroll( hEditWnd , iLines , 0 ) ;
        free( cBuf ) ;
    }
}

void vConsole_Debug( void )
{
    char *cBuf ;
    int iLoop ;
    FILE *ofp ;

    cBuf = (char *)malloc(DEF_CONSOLE_MAX_CHAR*DEF_CONSOLE_MAX_LINE) ;
    cBuf[0] = 0 ;
    if ( cBuf )
    {
        if ( iConsoleLoop )
        {
            if ( iConsoleEnd < DEF_CONSOLE_MAX_LINE-1 )
            {
                for ( iLoop = iConsoleEnd+1 ; iLoop < DEF_CONSOLE_MAX_LINE ; iLoop ++ )
                {
                    strcat( cBuf , stcConsoleLineRoot[iLoop].cData ) ;
                    strcat( cBuf , "\r\n" ) ;
                }
            }
        }
        for ( iLoop = 0 ; iLoop < iConsoleEnd ; iLoop ++ )
        {
            strcat( cBuf , stcConsoleLineRoot[iLoop].cData ) ;
            strcat( cBuf , "\r\n" ) ;
        }
        ofp = fopen( "d:\\work\\debug.txt" , "wb" ) ;
        if ( ofp )
        {
            fprintf( ofp , "%s" , cBuf ) ;
            fclose( ofp ) ;
        }
        free( cBuf ) ;
    }
}
extern int iTestStartGetNumberReady ;
extern char cTestNumberName[64] ;
void vConsole_Save( const char *cStr , int iLength )
{
    int iLoop ;
    CONSOLE_LINE *pLine ;

    if ( iLength )
    {
            FILE *ofp ;

            ofp = fopen( cTestNumberName , "a+" ) ;
            if ( ofp )
            {
                fwrite( cStr , 1 , iLength , ofp );
                fclose( ofp ) ;
            }
    }
}
