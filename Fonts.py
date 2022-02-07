import os
import sys
from ctypes import wintypes

import ctypes, sys
try:
    import winreg
except ImportError:
    import _winreg as winreg

user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)

FONTS_REG_PATH = r'Software\Microsoft\Windows NT\CurrentVersion\Fonts'

HWND_BROADCAST = 0xFFFF
SMTO_ABORTIFHUNG = 0x0002
WM_FONTCHANGE = 0x001D
GFRI_DESCRIPTION = 1
GFRI_ISTRUETYPE = 3

if not hasattr(wintypes, 'LPDWORD'):
    wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

user32.SendMessageTimeoutW.restype = wintypes.LPVOID
user32.SendMessageTimeoutW.argtypes = (
    wintypes.HWND,   # hWnd
    wintypes.UINT,   # Msg
    wintypes.LPVOID, # wParam
    wintypes.LPVOID, # lParam
    wintypes.UINT,   # fuFlags
    wintypes.UINT,   # uTimeout
    wintypes.LPVOID  # lpdwResult
)

gdi32.AddFontResourceW.argtypes = (
    wintypes.LPCWSTR,) # lpszFilename

gdi32.GetFontResourceInfoW.argtypes = (
    wintypes.LPCWSTR, # lpszFilename
    wintypes.LPDWORD, # cbBuffer
    wintypes.LPVOID,  # lpBuffer
    wintypes.DWORD)   # dwQueryType


def load_font(font_path):

    # load the font in the current session
    if not gdi32.AddFontResourceW(font_path):
        raise WindowsError(f"AddFontResource failed to load {font_path}")

    # notify all the  running programs that a font file has been loaded so that they can use it 
    user32.SendMessageTimeoutW(
        HWND_BROADCAST, WM_FONTCHANGE, 0, 0, SMTO_ABORTIFHUNG, 1000, None
    )
    
def main(font_files):
    for font_file in font_files:
        if os.path.exists(font_file):
            if font_file.endswith('.otf') or font_file.endswith('.ttf'):
                print('Installing ' + font_file)
                load_font(font_file)
        else:
            raise FileNotFoundError


def load_fonts():
    main([r"ds_digital\DS-DIGI.ttf",r"ds_digital\DS-DIGIB.ttf"])


    
if __name__ == '__main__':
    load_fonts()
