# This is a mini project implementing transactional log on data files

## Architecture of the code
mini_delta/
├── mini_delta.py         ← Core logic (insert, read, history)
├── transformations.py    ← (Future) Transformations on top of stored data
├── cli.py                ← CLI wrapper using Typer
├── utils.py              ← (Optional) Helper functions (schema check, etc.)
├── examples/
│   ├── load_data.py      ← Example: insert and read
│   └── transform_query.sql
└── data/
    └── sales_table/      ← Example: actual MiniDelta table with _delta_log
