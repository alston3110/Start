# -*- coding: utf-8 -*-

import ctypes

int = ctypes.c_int

BOOL = ctypes.c_int
DWORD = ctypes.c_uint32
UINT = ctypes.c_uint32
LONG = ctypes.c_int32
WPARAM = ctypes.c_uint32
LPARAM = ctypes.c_int32
LRESULT = ctypes.c_int32
LARGE_INTEGER = ctypes.c_int64

HANDLE = ctypes.c_void_p
HWND = ctypes.c_void_p
HDC = ctypes.c_void_p
HMENU = HANDLE
HINSTANCE = HANDLE
HMODULE = HANDLE
ATOM = ctypes.c_uint16
HICON = HANDLE
HCURSOR = HANDLE
HBRUSH = HANDLE
WNDPROC = ctypes.WINFUNCTYPE(LRESULT, HWND, UINT, WPARAM, LPARAM)

LPVOID = ctypes.c_void_p
LPCSTR = ctypes.c_char_p
