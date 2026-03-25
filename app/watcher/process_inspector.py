import psutil
import win32gui
import  win32process

from dataclasses import dataclass
from typing import Optional
from app.watcher.handlers.notepad_handler import NotepadHandler

@dataclass
class InspectionResult:
    app_name: str
    exe_path: str
    file_path: Optional[str]
    extension: Optional[str]

# Handler registry for supported applications

APP_HANDLERS = {
    "notepad.exe": NotepadHandler(),
}

class ProcessInspector:
    def get_active_window_info(self) -> Optional[InspectionResult]:
        hwnd = win32gui.GetForegroundWindow()
        if not hwnd:
            return None

        # Window title
        window_title = win32gui.GetWindowText(hwnd)

        # Process ID
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        try:
            process = psutil.Process(pid)
        except psutil.NoSuchProcess:
            return None

        exe_name = process.name().lower()
        exe_path = process.exe()

        # Select handler
        handler = APP_HANDLERS.get(exe_name)

        # Extract file path if handler exists
        file_path = handler.extract_file(window_title) if handler else None

        # Determine extension
        extension = None
        if file_path and "." in file_path:
            extension = file_path.split(".")[-1].lower()

        return InspectionResult(
            app_name=exe_name,
            exe_path=exe_path,
            file_path=file_path,
            extension=extension,
        )



def get_active_process_info():
    hwnd = win32gui.GetForegroundWindow()
    if not hwnd:
        return None, None, None

    # Get window title
    window_title = win32gui.GetWindowText(hwnd)

    # Get process ID
    _, pid = win32process.GetWindowThreadProcessId(hwnd)

    # Get process object
    try:
        process = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return None, None, None

    exe_name = process.name().lower()
    exe_path = process.exe()

    return window_title, exe_name, exe_path


