# encoding: utf-8
# module matplotlib._c_internal_utils
# from C:\Users\mr855\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\matplotlib\_c_internal_utils.cp310-win_amd64.pyd
# by generator 1.147
# no doc
# no imports

# functions

def display_is_valid(*args, **kwargs): # real signature unknown
    """
    Check whether the current X11 or Wayland display is valid.
    
    On Linux, returns True if either $DISPLAY is set and XOpenDisplay(NULL)
    succeeds, or $WAYLAND_DISPLAY is set and wl_display_connect(NULL)
    succeeds.
    
    On other platforms, always returns True.
    """
    pass

def Win32_GetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows's GetCurrentProcessExplicitAppUserModelID.
    
    On non-Windows platforms, always returns None.
    """
    pass

def Win32_GetForegroundWindow(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows' GetForegroundWindow.
    
    On non-Windows platforms, always returns None.
    """
    pass

def Win32_SetCurrentProcessExplicitAppUserModelID(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows's SetCurrentProcessExplicitAppUserModelID.
    
    On non-Windows platforms, does nothing.
    """
    pass

def Win32_SetForegroundWindow(*args, **kwargs): # real signature unknown
    """
    Wrapper for Windows' SetForegroundWindow.
    
    On non-Windows platforms, does nothing.
    """
    pass

def Win32_SetProcessDpiAwareness_max(*args, **kwargs): # real signature unknown
    """
    Set Windows' process DPI awareness to best option available.
    
    On non-Windows platforms, does nothing.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D63D6655A0>'

__spec__ = None # (!) real value is "ModuleSpec(name='matplotlib._c_internal_utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x000001D63D6655A0>, origin='C:\\\\Users\\\\mr855\\\\AppData\\\\Local\\\\Packages\\\\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\\\\LocalCache\\\\local-packages\\\\Python310\\\\site-packages\\\\matplotlib\\\\_c_internal_utils.cp310-win_amd64.pyd')"

