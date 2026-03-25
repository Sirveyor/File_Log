┌──────────────────────────────────────────────────────────────┐
│                    1. USER ACTION (Trigger)                  │
│  You open a file, switch windows, close a file, etc.         │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│        2. WINDOWS EVENT LAYER (Foreground Change)            │
│  • Win32 hook fires: "active window changed"                 │
│  • Captures:                                                 │
│       - window handle                                        │
│       - process ID                                           │
│       - window title                                         │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│            3. PROCESS INSPECTION (psutil/pywin32)            │
│  • Using PID:                                                │
│       - get exe path                                         │
│       - scan open file handles                               │
│       - extract candidate file paths                         │
│  • Apply app-specific rules (VS Code, AutoCAD, etc.)         │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                4. FILE SESSION TRACKER (Python)              │
│  • Compares new active file to previous active file          │
│  • If different:                                             │
│       - close previous session                               │
│       - open new session                                     │
│  • Handles edge cases:                                       │
│       - app crash                                            │
│       - file reopened                                        │
│       - switching tabs in same app                           │
│       - temp files                                           │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                   5. DATABASE WRITE (SQLite)                 │
│  • Insert/update:                                            │
│       - apps table                                           │
│       - files table                                          │
│       - sessions table                                       │
│  • Session row includes:                                     │
│       - file_id                                              │
│       - app_id                                               │
│       - opened_at                                            │
│       - closed_at (when known)                               │
│       - duration_seconds                                     │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                     6. ANALYTICS & OUTPUT                    │
│  • Daily summary                                             │
│  • Weekly/monthly reports                                    │
│  • TUI dashboard views                                       │
│  • Optional CSV/JSON export                                  │
└──────────────────────────────────────────────────────────────┘