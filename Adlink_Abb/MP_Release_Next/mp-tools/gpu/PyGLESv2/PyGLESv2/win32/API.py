# -*- coding: utf-8 -*-

import ctypes
from Type import *

NULL = ctypes.c_void_p(0)

CS_VREDRAW          = 0x0001
CS_HREDRAW          = 0x0002
CS_DBLCLKS          = 0x0008
CS_OWNDC            = 0x0020
CS_CLASSDC          = 0x0040
CS_PARENTDC         = 0x0080
CS_NOCLOSE          = 0x0200
CS_SAVEBITS         = 0x0800
CS_BYTEALIGNCLIENT  = 0x1000
CS_BYTEALIGNWINDOW  = 0x2000
CS_GLOBALCLASS      = 0x4000


WS_OVERLAPPED       = 0x00000000L
WS_POPUP            = 0x80000000L
WS_CHILD            = 0x40000000L
WS_MINIMIZE         = 0x20000000L
WS_VISIBLE          = 0x10000000L
WS_DISABLED         = 0x08000000L
WS_CLIPSIBLINGS     = 0x04000000L
WS_CLIPCHILDREN     = 0x02000000L
WS_MAXIMIZE         = 0x01000000L
WS_CAPTION          = 0x00C00000L
WS_BORDER           = 0x00800000L
WS_DLGFRAME         = 0x00400000L
WS_VSCROLL          = 0x00200000L
WS_HSCROLL          = 0x00100000L
WS_SYSMENU          = 0x00080000L
WS_THICKFRAME       = 0x00040000L
WS_GROUP            = 0x00020000L
WS_TABSTOP          = 0x00010000L

WS_MINIMIZEBOX      = 0x00020000L
WS_MAXIMIZEBOX      = 0x00010000L

WS_OVERLAPPEDWINDOW = WS_OVERLAPPED     | \
                      WS_CAPTION        | \
                      WS_SYSMENU        | \
                      WS_THICKFRAME     | \
                      WS_MINIMIZEBOX    | \
                      WS_MAXIMIZEBOX

WS_POPUPWINDOW      = WS_POPUP          | \
                      WS_BORDER         | \
                      WS_SYSMENU

WS_CHILDWINDOW      = WS_CHILD

WS_TILED            = WS_OVERLAPPED
WS_ICONIC           = WS_MINIMIZE
WS_SIZEBOX          = WS_THICKFRAME
WS_TILEDWINDOW      = WS_OVERLAPPEDWINDOW


WS_EX_DLGMODALFRAME     = 0x00000001L
WS_EX_NOPARENTNOTIFY    = 0x00000004L
WS_EX_TOPMOST           = 0x00000008L
WS_EX_ACCEPTFILES       = 0x00000010L
WS_EX_TRANSPARENT       = 0x00000020L
#if(WINVER >= 0x0400)
WS_EX_MDICHILD          = 0x00000040L
WS_EX_TOOLWINDOW        = 0x00000080L
WS_EX_WINDOWEDGE        = 0x00000100L
WS_EX_CLIENTEDGE        = 0x00000200L
WS_EX_CONTEXTHELP       = 0x00000400L

WS_EX_RIGHT             = 0x00001000L
WS_EX_LEFT              = 0x00000000L
WS_EX_RTLREADING        = 0x00002000L
WS_EX_LTRREADING        = 0x00000000L
WS_EX_LEFTSCROLLBAR     = 0x00004000L
WS_EX_RIGHTSCROLLBAR    = 0x00000000L

WS_EX_CONTROLPARENT     = 0x00010000L
WS_EX_STATICEDGE        = 0x00020000L
WS_EX_APPWINDOW         = 0x00040000L

WS_EX_OVERLAPPEDWINDOW  = (WS_EX_WINDOWEDGE | WS_EX_CLIENTEDGE)
WS_EX_PALETTEWINDOW     = (WS_EX_WINDOWEDGE | WS_EX_TOOLWINDOW | WS_EX_TOPMOST)

#endif

#if(_WIN32_WINNT >= 0x0500)
WS_EX_LAYERED           = 0x00080000
#endif

#if(WINVER >= 0x0500)
WS_EX_NOINHERITLAYOUT   = 0x00100000L # Disable inheritence of mirroring by children
WS_EX_LAYOUTRTL         = 0x00400000L # Right to left mirroring
#endif /* WINVER >= 0x0500 */

#if(_WIN32_WINNT >= 0x0501)
WS_EX_COMPOSITED        = 0x02000000L
#endif /* _WIN32_WINNT >= 0x0501 */
#if(_WIN32_WINNT >= 0x0500)
WS_EX_NOACTIVATE        = 0x08000000L
#endif /* _WIN32_WINNT >= 0x0500 */

CW_USEDEFAULT       = (0x80000000)

PM_NOREMOVE         = 0x0000
PM_REMOVE           = 0x0001
PM_NOYIELD          = 0x0002

#hWnd = CreateWindowEx(
#        WS_EX_LEFT, TEXT("STATIC"), TEXT("なんくるないさー"),
#        WS_OVERLAPPEDWINDOW | WS_VISIBLE,
#        CW_USEDEFAULT, CW_USEDEFAULT, 400, 300,
#        NULL, NULL, hInstance, NULL
#    );


class POINT(ctypes.Structure):
    _fields_ = [("x", LONG),
                ("y", LONG)]

class RECT(ctypes.Structure):
    _fields_ = [("left", LONG),
                ("top", LONG),
                ("right", LONG),
                ("bottom", LONG)]

class MSG(ctypes.Structure):
    _fields_ = [("hwnd", HWND),
                ("message", UINT),
                ("wParam", WPARAM),
                ("lParam", LPARAM),
                ("time", DWORD),
                ("pt", POINT)]

class WNDCLASSEX(ctypes.Structure):
    _fields_ = [('cbSize', UINT),
                ('style', UINT),
                ('lpfnWndProc', WNDPROC),
                ('cbClsExtra', int),
                ('cbWndExtra', int),
                ('hInstance', HINSTANCE),
                ('hIcon', HICON),
                ('hCursor', HCURSOR),
                ('hbrBackground', HBRUSH),
                ('lpszMenuName', LPCSTR),
                ('lpszClassName', LPCSTR),
                ('hIconSm', HICON)]

GetModuleHandle = ctypes.windll.kernel32.GetModuleHandleA
GetModuleHandle.argtypes = (ctypes.c_int, )
GetModuleHandle.restype = HMODULE

RegisterClassEx = ctypes.windll.user32.RegisterClassExA
RegisterClassEx.argtypes = (ctypes.POINTER(WNDCLASSEX),)
RegisterClassEx.restype = ATOM

CreateWindowEx = ctypes.windll.user32.CreateWindowExA
CreateWindowEx.argtypes = [DWORD, LPCSTR, LPCSTR, DWORD, int, int, int, int, HWND, HMENU, HINSTANCE, LPVOID]
CreateWindowEx.restype = HWND

DestroyWindow = ctypes.windll.user32.DestroyWindow
DestroyWindow.argtypes = (HWND,)
DestroyWindow.restype = BOOL

PeekMessage = ctypes.windll.user32.PeekMessageA
PeekMessage.argtypes = (ctypes.POINTER(MSG), HWND, UINT, UINT, UINT)
PeekMessage.restype = BOOL

GetMessage = ctypes.windll.user32.GetMessageA
GetMessage.argtypes = (ctypes.POINTER(MSG), HWND, UINT, UINT)
GetMessage.restype = BOOL

DefWindowProc = ctypes.windll.user32.DefWindowProcA
DefWindowProc.argtypes = (HWND, UINT, WPARAM, LPARAM)
DefWindowProc.restype = LRESULT

TranslateMessage = ctypes.windll.user32.TranslateMessage
TranslateMessage.argtypes = (ctypes.POINTER(MSG),)
TranslateMessage.restype = BOOL

DispatchMessage = ctypes.windll.user32.DispatchMessageA
DispatchMessage.argtypes = (ctypes.POINTER(MSG),)
DispatchMessage.restype = LRESULT

QueryPerformanceCounter = ctypes.windll.kernel32.QueryPerformanceCounter
QueryPerformanceCounter.argtypes = (ctypes.POINTER(LARGE_INTEGER),)
QueryPerformanceCounter.restype = BOOL

QueryPerformanceFrequency = ctypes.windll.kernel32.QueryPerformanceFrequency
QueryPerformanceFrequency.argtypes = (ctypes.POINTER(LARGE_INTEGER),)
QueryPerformanceFrequency.restype = BOOL

PostQuitMessage = ctypes.windll.user32.PostQuitMessage
PostQuitMessage.argtypes = (int,)
PostQuitMessage.restype = None

Sleep = ctypes.windll.kernel32.Sleep
Sleep.argtypes = (DWORD,)
Sleep.restype = None

ValidateRect = ctypes.windll.user32.ValidateRect
ValidateRect.argtypes = (HWND, ctypes.c_void_p)
ValidateRect.restype = BOOL

GetCursorPos = ctypes.windll.user32.GetCursorPos
GetCursorPos.argtypes = (ctypes.POINTER(POINT),)
GetCursorPos.restype = BOOL

SendMessage = ctypes.windll.user32.SendMessageA
SendMessage.argtypes = (HWND, UINT, WPARAM, LPARAM)
SendMessage.restype = LRESULT

GetDC = ctypes.windll.user32.GetDC
GetDC.argtypes = (HWND,)
GetDC.restype = HDC

