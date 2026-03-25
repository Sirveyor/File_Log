┌──────────────────────────────────────────────────────────────┐
│                        USER WORKFLOW                         │
│  (You open/close files in VS Code, AutoCAD, Notepad, etc.)   │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                WINDOWS EVENT + PROCESS LAYER                 │
│                                                              │
│  • Foreground Window Listener (Win32 API)                    │
│  • Process Inspector (psutil / pywin32)                      │
│  • File Handle Scanner                                       │
│                                                              │
│  Purpose: Detect which app is active and what file(s)        │
│  the process currently has open.                             │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                 FILE SESSION TRACKER (Python)                │
│                                                              │
│  • Determines when a file session starts                     │
│  • Determines when a session ends                            │
│  • Tracks:                                                   │
│       - file path                                            │
│       - application                                          │
│       - opened_at                                            │
│       - closed_at                                            │
│       - duration                                             │
│                                                              │
│  • Handles edge cases:                                       │
│       - app crashes                                          │
│       - file reopened                                        │
│       - switching between files in same app                  │
│       - temp files                                           │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                     DATA STORAGE LAYER                       │
│                        (SQLite DB)                           │
│                                                              │
│  Tables:                                                     │
│    apps:     id | name | exe_path                            │
│    files:    id | path | extension                           │
│    sessions: id | file_id | app_id | opened_at | closed_at   │
│                                                              │
│  Purpose: Durable, queryable history of your daily work.     │
└──────────────────────────────────────────────────────────────┘
                               │
                               ▼
┌──────────────────────────────────────────────────────────────┐
│                     ANALYTICS & OUTPUT                       │
│                                                              │
│  • Daily summary (files used, durations)                     │
│  • Weekly/monthly reports                                    │
│  • TUI dashboard (fits your suite perfectly)                 │
│  • Optional export to CSV/JSON                               │
│  • Optional integration with your existing launcher          │
└──────────────────────────────────────────────────────────────┘