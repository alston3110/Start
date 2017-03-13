#include "../include/common.h"

/* ------------------------------------------------------------------------- */
extern HWND hMainWnd ;

/* ------------------------------------------------------------------------- */
int          ubRS232IsExist = 0 ;
HANDLE       hRS232ComHandle ;
DCB          dcbRS232DCBInfo ;
COMMPROP     cRS232Info ;
COMMTIMEOUTS RS232TimeOut ;

/* ------------------------------------------------------------------------- */
void vRS232_Open( const char *cComPort )
{
    if ( hRS232ComHandle != NULL )
	{
		CloseHandle( hRS232ComHandle ) ;
		hRS232ComHandle = NULL ;
	}
	hRS232ComHandle = CreateFile( (const char *)cComPort , GENERIC_READ|GENERIC_WRITE,0,NULL,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL,NULL);
}

void vRS232_Close( void )
{
    ubRS232IsExist = 0 ;
    if ( hRS232ComHandle != NULL )
	{
		CloseHandle( hRS232ComHandle ) ;
		hRS232ComHandle = NULL ;
	}
}

void vRS232_BuildCommDCB( void )
{
	char ubSetInfo[512] ;

	strcpy((char *)ubSetInfo , (const char *)"baud=115200 parity=N data=8 stop=1" ) ;

    BuildCommDCB( (const char *)ubSetInfo , &dcbRS232DCBInfo ) ;
}

void vRS232_SetState( void )
{
    if ( hRS232ComHandle != NULL )
	{
		SetCommState( hRS232ComHandle , &dcbRS232DCBInfo ) ;
	}
}

void vRS232_SetTimeOut( void )
{
    RS232TimeOut.ReadIntervalTimeout         = MAXDWORD ; // MAXDWORD
	RS232TimeOut.ReadTotalTimeoutMultiplier  = 0 ;
	RS232TimeOut.ReadTotalTimeoutConstant    = 0 ;
	RS232TimeOut.WriteTotalTimeoutConstant   = 0 ;
	RS232TimeOut.WriteTotalTimeoutMultiplier = 0 ;
    if ( hRS232ComHandle != NULL )
    {
		SetCommTimeouts( hRS232ComHandle , &RS232TimeOut ) ;
	}
}

void vRS232_Start( const char *cPort )
{
    ubRS232IsExist = 0 ;

    vRS232_Open( cPort ) ;
	vRS232_BuildCommDCB( ) ;
	vRS232_SetState( ) ;
	vRS232_SetTimeOut( ) ;
    ubRS232IsExist = 1 ;
}

long ulRS232_Read( unsigned char *ubData , long ulBytes )
{
    if ( ubRS232IsExist )
    {
        if ( ReadFile( hRS232ComHandle , ubData , ulBytes , (unsigned long *)&ulBytes , NULL ) )
        {
            return ( ulBytes ) ;
        }
        else
        {
            if ( GetLastError( ) != ERROR_IO_PENDING )
            {
                SendMessage( hMainWnd , WM_USER1 , 0 , 0 ) ;
                vRS232_Close( ) ;
            }
        }
    }
    return ( 0 ) ;
}

void vRS232_Write( unsigned char *ubData , long ulBytes )
{
    if ( ubRS232IsExist )
    {
        if ( !WriteFile( hRS232ComHandle , ubData , ulBytes , (unsigned long *)&ulBytes , NULL ) )
        {
            if ( GetLastError( ) != ERROR_IO_PENDING )
            {
                SendMessage( hMainWnd , WM_USER1 , 0 , 0 ) ;
                vRS232_Close( ) ;
            }
        }
    }
}

void vRS232_GetInfo( void )
{
    if ( hRS232ComHandle != NULL )
    {
        GetCommProperties( hRS232ComHandle , &cRS232Info ) ;
    }
}

int iRS232_ListPorts( HWND hComboWnd )
{
    HKEY hKey;

    long dwErrorCode = ::RegOpenKeyEx( HKEY_LOCAL_MACHINE , "HARDWARE\\DEVICEMAP\\SERIALCOMM\\" , 0 , KEY_READ , &hKey ) ;

    if( dwErrorCode != ERROR_SUCCESS )
    {
        return ( 0 ) ;
    }
    CHAR  Name[25];
    UCHAR szPortName[25];
    LONG  Status;
    DWORD dwIndex = 0;
    DWORD dwName;
    DWORD dwSizeofPortName;
    DWORD Type;
    int   iNumber = 0 ;

    dwName = sizeof(Name);
    dwSizeofPortName = sizeof(szPortName);
    do
    {
        Status = RegEnumValue(hKey, dwIndex++, Name, &dwName, NULL, &Type,szPortName, &dwSizeofPortName);

        if((Status == ERROR_SUCCESS)||(Status == ERROR_MORE_DATA))
        {
            SendMessage( hComboWnd , CB_ADDSTRING , 0 , reinterpret_cast<LPARAM>( (LPCTSTR)szPortName ) ) ;
            iNumber ++ ;
        }
    } while((Status == ERROR_SUCCESS)||(Status == ERROR_MORE_DATA));

    RegCloseKey(hKey);
    return ( iNumber ) ;
}
