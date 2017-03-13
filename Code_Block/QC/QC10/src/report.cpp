#include "../include/common.h"

/* ------------------------------------------------------------------------- */
extern HINSTANCE hMainInst ;
extern HWND      hMainWnd  ;

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
    LV_COLUMN stcLVC ;
    int iLoop ;
    const REPORT_COLUMN stcColumnData[] = {
        {
            IDS_STRING_REPORT_ITEM ,
            435
        } ,
        {
            IDS_STRING_REPORT ,
            80
        }
    } ;

    stcLVC.mask = LVCF_TEXT | LVCF_WIDTH;
    for ( iLoop = 0 ; iLoop < (int)( sizeof( stcColumnData ) / sizeof(REPORT_COLUMN) ) ; iLoop ++ )
    {
        TCHAR szTempStr[32] ;

        LoadString( hMainInst , stcColumnData[iLoop].iStr , szTempStr , 32 ) ;
        stcLVC.pszText = szTempStr   ;
        stcLVC.cx      = stcColumnData[iLoop].iWidth ;
        SendMessage( hWnd , LVM_INSERTCOLUMN , iLoop , (long)&stcLVC ) ;
    }
}

void vReport_InsertItems( HWND hWnd )
{
    int iLoop ;
    LVITEM stcLVI ;

    // Initialize LVITEM members that are common to all items.
    stcLVI.mask      = LVIF_TEXT ;
    stcLVI.stateMask = 0;
    stcLVI.state     = 0;

    // Initialize LVITEM members that are different for each item.
    for ( iLoop = 0; iLoop < (int)( sizeof(stcItem) / sizeof(REPORT_ITEM)) ; iLoop++ )
    {
        stcLVI.pszText  = (LPSTR)stcItem[iLoop].cStr ;
        stcLVI.iSubItem = 0 ;
        stcLVI.iItem    = iLoop ;

        ListView_InsertItem( hWnd, &stcLVI ) ;

        stcLVI.pszText  = (LPSTR)stcItem[iLoop].cState ;
        stcLVI.iSubItem = 1 ;
        stcLVI.iItem    = iLoop ;

        ListView_SetItem( hWnd, &stcLVI ) ;
    }
}

void vReport_Init( HWND hWnd )
{
    ListView_SetExtendedListViewStyle( hWnd , LVS_EX_GRIDLINES ) ;
    vReport_InitColumn( hWnd ) ;
    vReport_InsertItems( hWnd ) ;
}

void vReport_SetInfo( int iItem , const char *cStr )
{
    if ( cStr )
    {
        if ( iItem < ( sizeof(stcItem) / sizeof(REPORT_ITEM)) )
        {
            ListView_SetItemText( GetDlgItem( hMainWnd , IDC_LIST_REPORT ) , iItem , 1 , (LPSTR)cStr ) ;
            if (!(strcmp(cStr,"PASS")))
                    ListView_SetTextColor(  GetDlgItem( hMainWnd , IDC_LIST_REPORT ) , 0x00FF0000);
            else if (!(strcmp(cStr,"FAIL")))
                    ListView_SetTextColor(  GetDlgItem( hMainWnd , IDC_LIST_REPORT ) , 0x000000FF);
            else
                    ListView_SetTextColor(  GetDlgItem( hMainWnd , IDC_LIST_REPORT ) , 0x00000000);
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
