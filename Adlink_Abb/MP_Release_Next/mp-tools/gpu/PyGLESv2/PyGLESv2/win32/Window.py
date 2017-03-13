# -*- coding: utf-8 -*-

import ctypes
from Type import *
from API import *
from Message import *

_WINDOW_CLASS='PyGLES2 Window'

DEFAULT_X = CW_USEDEFAULT
DEFAULT_Y = CW_USEDEFAULT
DEFAULT_WIDTH = 640
DEFAULT_HEIGHT = 480

class Window(object):
    '''
    classdocs
    '''

    def __init__(self, name, x = DEFAULT_X, y = DEFAULT_Y, width = DEFAULT_WIDTH, height = DEFAULT_HEIGHT):
        '''
        Constructor
        '''

        self.event_driven = False

        def callback_proxy(hWnd, msg, wParam, lParam):
            if msg == WM_PAINT:
                self.onPaint()
                ValidateRect(hWnd, NULL)
                return 0
            elif msg == WM_CHAR:
                point = POINT()
                GetCursorPos(ctypes.byref(point))
                self.onKeyEvent(wParam, point.x, point.y)
                return 0
            elif msg == WM_ERASEBKGND:
                return 0
            elif msg == WM_DESTROY:
                PostQuitMessage(0)
                return 0
            return DefWindowProc(hWnd, msg, wParam, lParam)

        self.my_callback = WNDPROC(callback_proxy)

        wnd = WNDCLASSEX()
        wnd.cbSize = ctypes.sizeof(WNDCLASSEX)
        wnd.style = CS_HREDRAW | CS_VREDRAW
        wnd.lpfnWndProc = self.my_callback
        wnd.cbClsExtra = 0
        wnd.cbWndExtra = 0
        wnd.hInstance = 0#GetModuleHandle(0)
        wnd.hIcon = 0
        wnd.hCursor = 0
        wnd.hbrBackground = 0
        wnd.lpszMenuName = 0
        wnd.lpszClassName = _WINDOW_CLASS
        wnd.hIconSm = 0

        RegisterClassEx(ctypes.byref(wnd))
        self.hwnd = CreateWindowEx(
            WS_EX_LEFT,
            _WINDOW_CLASS,
            name,
            WS_OVERLAPPEDWINDOW | WS_VISIBLE,
            x, y,
            width, height,
            0,
            0,
            0,
            0)

    def __del__(self):
        print "destroy_window."
        DestroyWindow(self.hwnd)

    def setEventDrivenMode(self, event_driven):
        self.event_driven = event_driven

    def run(self):
        infinite_loop = True
        msg = MSG()
        
        self.onInit()
        self.onIdle()

        if self.event_driven:
            while infinite_loop:
                ret = GetMessage(ctypes.byref(msg), 0, 0, 0)
                if 0 < ret:
                    TranslateMessage(ctypes.byref(msg))
                    DispatchMessage(ctypes.byref(msg))
                else:
                    infinite_loop = False
        else:
            while infinite_loop:
                ret = PeekMessage(ctypes.byref(msg), 0, 0, 0, PM_REMOVE)
                if 0 < ret:
                    TranslateMessage(ctypes.byref(msg))
                    DispatchMessage(ctypes.byref(msg))
                elif 0 == ret and msg.message != WM_QUIT:
                    self.onIdle()
                else:
                    infinite_loop = False

        self.onExit()

        return msg.wParam

    def getHandle(self):
        return self.hwnd

    def getDisplayId(self):
        return GetDC(self.hwnd)

    def onPaint(self):
        return 0

    def onIdle(self):
        return 0

    def onInit(self):
        pass
    
    def onExit(self):
        pass

__freq = LARGE_INTEGER()
QueryPerformanceFrequency(ctypes.byref(__freq))
_freq = __freq.value
def get_tick():
    value = LARGE_INTEGER()
    QueryPerformanceCounter(ctypes.byref(value))
    return value.value * 1000 / _freq

def Main():
    import sys
    #print windll.user32.CreateWindowExA
    my = Window("MyWindow", CW_USEDEFAULT, CW_USEDEFAULT, 640, 480)
    return my.run()
#    raw_input()
    pass

if __name__ == "__main__":
    Main()
