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
    char *cTime  ;
} REPORT_ITEM ;

/* ------------------------------------------------------------------------- */
const REPORT_ITEM stcItem[] = {
    { (char *)"01  - LED(GPIO)          -- LED閃爍是否正確"                 , (char *)"N/A" , (char *)"N/A" } ,
//    { (char *)"02  - BUTTON        -- Button是否正確點亮LED"                  , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"02  - Vedio(LVDS)   ---------- 影像輸出是否正確"                                           , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"03  - 3AXIS                 -- 三軸輸出是否正確"              , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"04  - SPI (Flash)"                                      , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"05  - AUDIO(I2C Read register)"                  , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"06  - USB(USB1)"                               , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"07  - SDCARD(SD1,SD2)"                                       , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"08  - RS232(UART4,UART5)"                                    , (char *)"N/A" , (char *)"N/A" } ,
    { (char *)"09  - ETH0"                                                  , (char *)"N/A" , (char *)"N/A" } ,
} ;

/* ------------------------------------------------------------------------- */
void vReport_InitColumn( HWND hWnd )
{
    LV_COLUMN stcLVC = {0} ;
    int iLoop ;
    const REPORT_COLUMN stcColumnData[] = {
        {
            IDS_STRING_REPORT_ITEM ,
            676-90
        } ,
        {
            IDS_STRING_REPORT ,
            90
        } ,
        {
            IDS_STRING_REPORT_TIME ,
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

        stcLVI.mask      = LVIF_TEXT ;
        stcLVI.pszText  = (LPSTR)stcItem[iLoop].cTime ;
        stcLVI.iSubItem = 2 ;
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
        }
    }
}

void vReport_SetTime( int iItem , const char *cStr )
{
    if ( cStr )
    {
        if ( iItem < ( sizeof(stcItem) / sizeof(REPORT_ITEM)) )
        {
            ListView_SetItemText( GetDlgItem( hRunDlgWnd , IDC_LIST_REPORT ) , iItem , 2 , (LPSTR)cStr ) ;
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

    for ( iLoop = 0; iLoop < (int)( sizeof(stcItem) / sizeof(REPORT_ITEM)) ; iLoop++ )
    {
        vReport_SetTime( iLoop , stcItem[iLoop].cTime ) ;
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
