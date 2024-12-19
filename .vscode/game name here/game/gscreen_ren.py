"""renpy
init python:
"""
import ctypes

user32 = ctypes.windll.user32
current_window = ctypes.create_string_buffer(512)
screen_changed = 0

def get_active_window():
    hwnd = user32.GetForegroundWindow()
    if not hwnd:
        # No active window (e.g., application closing or Alt+F4)
        return None
    try:
        user32.GetWindowTextA(hwnd, current_window, 512)
        return current_window.value.decode('utf-8', errors='replace')  # Replace invalid characters
    except Exception as e:
        # Handle unexpected errors gracefully
        renpy.notify(f"Error getting window title: {e}")
        return None

previous_window = None  # Initialize with None for the first check

def check_window_focus():
    """Check if the active window has changed."""
    global previous_window
    active_window = get_active_window()

    if previous_window is None:
        # First-time setup
        previous_window = active_window

    if active_window is None:
        # Handle cases where there is no active window
        return  # Stop checking further to avoid issues
    
    if active_window != previous_window:
        global screen_changed
        screen_changed = 1
        #renpy.notify(f"Window changed: {previous_window} -> {active_window}")
        previous_window = active_window

    # Schedule the next check after 1 second
    renpy.pause(1.0, hard=False)
    renpy.call_in_new_context("check_window_focus_label")
