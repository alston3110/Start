#ifndef COMMON_H_INCLUDED
#define COMMON_H_INCLUDED

#include <windows.h>
#include <windowsx.h>
#include <commctrl.h>
#include <stdio.h>
#include <string.h>

#include "../resource.h"

#include "Timer.h"
#include "RS232.h"
#include "console.h"

#define WM_USER1 (WM_USER+1)
#define WM_USER2 (WM_USER+2)

typedef struct __CHECK_STR__ {
    unsigned char *pStr ;
    int            iIndex ;
    int            iState ;
    int            iFun   ;
} CHECK_STR ;

extern void vStatus_Show( const char *cStr ) ;
extern void vTimer_Show( const char *cStr ) ;

#endif // COMMON_H_INCLUDED
