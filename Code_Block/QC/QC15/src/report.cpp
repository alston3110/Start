#include "../include/common.h"

/* ------------------------------------------------------------------------- */
extern HINSTANCE hMainInst ;
extern HWND hRunDlgWnd ;

/* ------------------------------------------------------------------------- */
typedef struct __REPORT_COLUMN__ {
    int   iStr   ;
    int   iWidth ;
} REPORT_COLUMN ;

typedef struct __REPORT_ITEM__ {
    char *cStr   ;
    char *cState ;
} REPORT_ITEM ;

/* ------------------------------------------------------------------------- */
const REPORT_ITEM stcItem[] = {
    { (char *)"01  - LED   (01) ----------- LED閃爍是否正確"           , (char *)"N/A" } ,
    { (char *)"02  - GPIO  (13) ---------- 電壓偵測是否正確"           , (char *)"N/A" } ,
    { (char *)"03  - AUDIO (20) --------- 音樂播放是否正確"           , (char *)"N/A" } ,
    { (char *)"04  - LVDS  (22) ---------- 影像輸出是否正確"           , (char *)"N/A" } ,
    { (char *)"05  - 3AXIS (23) ---------- 三軸輸出是否正確"           , (char *)"N/A" } ,
    { (char *)"06  - TOUCHPANEL(24) -- 觸控面板輸出是否正確"       , (char *)"N/A" } ,
    { (char *)"07  - USB   (03)"           , (char *)"N/A" } ,
    { (char *)"08  - WIFI  (04)"           , (char *)"N/A" } ,
    { (char *)"09  - ETH0  (08)"           , (char *)"N/A" } ,
    { (char *)"10  - ETH1  (21)"           , (char *)"N/A" } ,
    { (char *)"11  - RS232 (10)"           , (char *)"N/A" } ,
    { (char *)"12  - DDR   (11)"           , (char *)"N/A" } ,
    { (char *)"13  - SDCARD(12)"           , (char *)"N/A" } ,
} ;

/* ------------------------------------------------------------------------- */
void vReport_InitColumn( HWND hWnd )
{
    LV_COLUMN stcLVC = {0} ;
    int iLoop ;
    const REPORT_COLUMN stcColumnData[] = {
        {
            IDS_STRING_REPORT_ITEM ,
            676
        } ,
        {
            IDS_STRING_REPORT ,
            90
        }
    } ;

    //ListView_InsertColumn( hWnd , 0 , &stcLVC ) ;

    stcLVC.mask = LVCF_TEXT | LVCF_WIDTH ;
    for ( iLoop = 0 ; iLoop < (int)( sizeof( stcColumnData ) / sizeof(REPORT_COLUMN) ) ; iLoop ++ )
    {
        TCHAR szTempStr[32] ;
        if ( stcColumnData[iLoop].iStr )
        {
            LoadString( hMainInst , stcColumnData[iLoop].iStr , szTempStr , 32 ) ;
            stcLVC.pszText = szTempStr   ;
        }
        else
        {
            stcLVC.pszText = 0 ;
        }
        stcLVC.cx      = stcColumnData[iLoop].iWidth ;
        ListView_InsertColumn( hWnd , iLoop+1 , &stcLVC ) ;
        //SendMessage( hWnd , LVM_INSERTCOLUMN , iLoop , (long)&stcLVC ) ;
    }
}

void vReport_InsertItems( HWND hWnd )
{
    int iLoop ;
    LVITEM stcLVI ;

    // Initialize LVITEM members that are common to all items.
    stcLVI.stateMask = 0;
    stcLVI.state     = 0;
/*
    HIMAGELIST hImageList = ImageList_Create( 16 , 16 , ILC_COLOR32 , 2 , 0 ) ;
    HICON hItem = LoadIcon( hMainInst , MAKEINTRESOURCE(IDI_ICON_EMPTY) ) ;
    ImageList_AddIcon( hImageList , hItem ) ;
    DeleteObject( hItem );
    hItem = LoadIcon( hMainInst , MAKEINTRESOURCE(IDI_ICON_OK) ) ;
    ImageList_AddIcon( hImageList , hItem ) ;
    DeleteObject( hItem );
    hItem = LoadIcon( hMainInst , MAKEINTRESOURCE(IDI_ICON_FAILE) ) ;
    ImageList_AddIcon( hImageList , hItem ) ;
    DeleteObject( hItem );
    hItem = LoadIcon( hMainInst , MAKEINTRESOURCE(IDI_ICON_RUN) ) ;
    ImageList_AddIcon( hImageList , hItem ) ;
    DeleteObject( hItem );
    ListView_SetImageList( hWnd , hImageList , LVSIL_SMALL ) ;
*/
    // Initialize LVITEM members that are different for each item.
    for ( iLoop = 0; iLoop < (int)( sizeof(stcItem) / sizeof(REPORT_ITEM)) ; iLoop++ )
    {
        stcLVI.mask      = LVIF_TEXT ;
        stcLVI.pszText  = (LPSTR)stcItem[iLoop].cStr ;
        stcLVI.iSubItem = 0 ;
        stcLVI.iItem    = iLoop ;
        stcLVI.iImage   = 0 ;

        ListView_InsertItem( hWnd, &stcLVI ) ;

        stcLVI.mask      = LVIF_TEXT ;
        stcLVI.pszText  = (LPSTR)stcItem[iLoop].cState ;
        stcLVI.iSubItem = 1 ;
        stcLVI.iItem    = iLoop ;
        stcLVI.iImage   = 0;

        ListView_SetItem( hWnd, &stcLVI ) ;

    }
}

void vReport_Init( HWND hWnd )
{
    ListView_SetExtendedListViewStyle( hWnd , LVS_EX_GRIDLINES | LVS_EX_CHECKBOXES | LVS_EX_FULLROWSELECT | LVS_EX_SUBITEMIMAGES ) ;
    //ListView_SetIconSpacing( hWnd , 128 , 128 ) ;
    vReport_InitColumn( hWnd ) ;
    vReport_InsertItems( hWnd ) ;

    {
        int iItem=SendMessage( hWnd , LVM_GETITEMCOUNT , 0 , 0 ) ;
        for ( int iLoop = 0 ; iLoop < iItem ; iLoop ++ )
        ListView_SetCheckState( hWnd , iLoop , 1 ) ;
    }
}

void vReport_SetInfo( int iItem , const char *cStr )
{
    if ( cStr )
    {
        if ( iItem < ( sizeof(stcItem) / sizeof(REPORT_ITEM)) )
        {
            ListView_SetItemText( GetDlgItem( hRunDlgWnd , IDC_LIST_REPORT ) , iItem , 1 , (LPSTR)cStr ) ;
            if (!(strcmp(cStr,"PASS")))
                    ListView_SetTextColor(  GetDlgItem( hRunDlgWnd , IDC_LIST_REPORT ) , 0x00FF0000);
            else if (!(strcmp(cStr,"FAIL")))
                    ListView_SetTextColor(  GetDlgItem( hRunDlgWnd , IDC_LIST_REPORT ) , 0x000000FF);
            else
                    ListView_SetTextColor(  GetDlgItem( hRunDlgWnd , IDC_LIST_REPORT ) , 0x00000000);
        }
    }
}

void vReport_SetNA( void )
{
    int iLoop ;

    for ( iLoop = 0; iLoop < (int)( sizeof(stcItem) / sizeof(REPORT_ITEM)) ; iLoop++ )
    {
        vReport_SetInfo( iLoop , stcItem[iLoop].cState ) ;
    }
}

int iReport_GetState( int iItem )
{
    if ( iItem < ( sizeof(stcItem) / sizeof(REPORT_ITEM)) )
    {
        return ( ListView_GetCheckState( GetDlgItem( hRunDlgWnd , IDC_LIST_REPORT ) , iItem ) ) ;
    }
    return ( 0 ) ;
}
