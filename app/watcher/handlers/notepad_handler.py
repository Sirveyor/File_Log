import os
from typing import Optional


class NotepadHandler:
    """
    Extracts the active file path from a Notepad window title.
    Returns an absolute path or None if the file cannot be determined.
    """

    SUFFIX = " - Notepad"
    READ_ONLY_SUFFIX = " (Read-Only)"

    def extract_file(self, window_title: str) -> Optional[str]:
        # Notepad titles always end with " - Notepad"
        if not window_title.endswith(self.SUFFIX):
            return None

        # Remove the suffix
        core = window_title[: -len(self.SUFFIX)]

        # Ignore unsaved documents
        if core == "Untitled":
            return None

        # Remove read-only marker if present
        if core.endswith(self.READ_ONLY_SUFFIX):
            core = core[: -len(self.READ_ONLY_SUFFIX)]

        # If the core contains a path separator, treat it as a full path
        if "\\" in core or "/" in core:
            return os.path.abspath(core)

        # If it's only a filename, Notepad doesn't expose the full path
        return None
