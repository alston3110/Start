#include "../include/common.h"

extern HINSTANCE hMainInst ;
extern BOOL CALLBACK bSettingDlg_Main(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam) ;
extern BOOL CALLBACK bRunDlg_Main(HWND hwndDlg, UINT uMsg, WPARAM wParam, LPARAM lParam) ;

char cMainTabNameStr[2][40] = {
	"ณ]ฉw",
	"ด๚ธี",
} ;

HWND hMainTabChildDlg[2] = { (HWND)NULL , (HWND)NULL } ;
int iMainTabNowNumber = 0 ;

void vMainTab_Init( HWND hwnd )
{
    HWND  hwndStatic ;
	TCITEM tci ;
	int iIndex ;

	hwndStatic = GetDlgItem( hwnd , IDC_TAB_MAIN ) ;
	tci.mask = TCIF_TEXT ;
	tci.iImage = -1 ;
	for ( iIndex = 0 ; iIndex < 2 ; iIndex ++ )
	{
		tci.pszText = cMainTabNameStr[iIndex] ;
		TabCtrl_InsertItem( hwndStatic , iIndex , &tci ) ;
	}

	hMainTabChildDlg[0] = CreateDialog( hMainInst , MAKEINTRESOURCE(IDD_SETTING) , hwndStatic , (DLGPROC)bSettingDlg_Main ) ;
	hMainTabChildDlg[1] = CreateDialog( hMainInst , MAKEINTRESOURCE(IDD_RUN)     , hwndStatic , (DLGPROC)bRunDlg_Main ) ;

    ShowWindow( hMainTabChildDlg[0] , SW_SHOW ) ;
    ShowWindow( hMainTabChildDlg[1] , SW_HIDE ) ;

    iMainTabNowNumber = 0 ;
}

void vMainTab_Select( HWND hwnd , LPNMHDR nmptr )
{
    HWND  hwndStatic ;
	int iTabNumber ;
//	HTREEITEM hObj ;

	if ( nmptr->code == TCN_SELCHANGE )
	{
		hwndStatic = GetDlgItem( hwnd , IDC_TAB_MAIN ) ;

		iTabNumber = TabCtrl_GetCurSel( (HWND)nmptr->hwndFrom ) ;
		if ( iTabNumber != iMainTabNowNumber )
        {
            ShowWindow( hMainTabChildDlg[iMainTabNowNumber] , SW_HIDE ) ;
            ShowWindow( hMainTabChildDlg[iTabNumber] , SW_SHOW ) ;
            iMainTabNowNumber = iTabNumber ;
        }
	}
}
/*
void vMainTab_Change( HWND hwnd )
{
    HWND  hwndStatic ;

	hwndStatic = GetDlgItem( hwnd , IDC_TAB_OPTION ) ;
	if ( hMainTabChildDlg != NULL )
	{
		DestroyWindow(hMainTabChildDlg) ;
		hMainTabChildDlg = NULL ;
	}
	switch( iMainTabNowNumber )
	{
		case 0 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_FILE_INFO) , hwndStatic , (DLGPROC)FileDlg_Process ) ;
			break ;
		case 1 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_PROTECT) , hwndStatic , (DLGPROC)ProtectDlg_Process ) ;
			break ;
		case 2 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_BOOT) , hwndStatic , (DLGPROC)BootDlg_Process ) ;
			break ;
		case 3 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_IO) , hwndStatic , (DLGPROC)IODlg_Process ) ;
			break ;
		case 4 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_SP) , hwndStatic , (DLGPROC)SPDlg_Process ) ;
			break ;
		case 5 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_GPU) , hwndStatic , (DLGPROC)GPUDlg_Process ) ;
			break ;
		case 6 :
			hMainTabChildDlg = CreateDialog( WindowsRecHinstance , MAKEINTRESOURCE(IDD_DIALOG_KEYPAD) , hwndStatic , (DLGPROC)KeyPadDlg_Process ) ;
			break ;
	}
}
*/

void vMainTab_Close( void )
{
	if ( hMainTabChildDlg[0] != NULL )
	{
		DestroyWindow(hMainTabChildDlg[0]) ;
		hMainTabChildDlg[0] = NULL ;
	}
	if ( hMainTabChildDlg[1] != NULL )
	{
		DestroyWindow(hMainTabChildDlg[1]) ;
		hMainTabChildDlg[1] = NULL ;
	}
}
