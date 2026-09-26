Lint report before fixes:

\*\*\*\*\*\*\*\*\*\*\*\*\* Module app.tasks

app/tasks.py:11:12: W1514: Using open without explicitly specifying an
encoding (unspecified-encoding)

app/tasks.py:11:12: R1732: Consider using \'with\' for
resource-allocating operations (consider-using-with)

app/tasks.py:19:9: W1514: Using open without explicitly specifying an
encoding (unspecified-encoding)

app/tasks.py:23:0: W0102: Dangerous default value \[\] as argument
(dangerous-default-value)

app/tasks.py:62:0: R1710: Either all return statements in a function
should return an expression, or none of them should.
(inconsistent-return-statements)

app/tasks.py:71:4: C0200: Consider using enumerate instead of iterating
with range and len (consider-using-enumerate)

app/tasks.py:79:4: R1705: Unnecessary \"else\" after \"return\", remove
the \"else\" and de-indent the code inside it (no-else-return)

app/tasks.py:79:7: C0121: Comparison \'is_premium == True\' should be
\'is_premium is True\' if checking for the singleton value True, or
\'is_premium\' if testing for truthiness (singleton-comparison)

\*\*\*\*\*\*\*\*\*\*\*\*\* Module app.cli

app/cli.py:6:0: C0116: Missing function or method docstring
(missing-function-docstring)

app/cli.py:2:0: W0611: Unused save_tasks imported from app.tasks
(unused-import)

app/cli.py:2:0: W0611: Unused add_task imported from app.tasks
(unused-import)

\*\*\*\*\*\*\*\*\*\*\*\*\* Module app.storage

app/storage.py:4:39: W0511: TODO: move to env var before release (fixme)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Your code has been rated at 8.33/10

Lint report after fixes:

\*\*\*\*\*\*\*\*\*\*\*\*\* Module app.tasks

app/tasks.py:12:17: W1514: Using open without explicitly specifying an
encoding (unspecified-encoding)

app/tasks.py:21:9: W1514: Using open without explicitly specifying an
encoding (unspecified-encoding)

app/tasks.py:74:4: C0200: Consider using enumerate instead of iterating
with range and len (consider-using-enumerate)

app/tasks.py:82:4: R1705: Unnecessary \"else\" after \"return\", remove
the \"else\" and de-indent the code inside it (no-else-return)

app/tasks.py:82:7: C0121: Comparison \'is_premium == True\' should be
\'is_premium is True\' if checking for the singleton value True, or
\'is_premium\' if testing for truthiness (singleton-comparison)

\*\*\*\*\*\*\*\*\*\*\*\*\* Module app.cli

app/cli.py:6:0: C0116: Missing function or method docstring
(missing-function-docstring)

app/cli.py:2:0: W0611: Unused save_tasks imported from app.tasks
(unused-import)

app/cli.py:2:0: W0611: Unused add_task imported from app.tasks
(unused-import)

\*\*\*\*\*\*\*\*\*\*\*\*\* Module app.storage

app/storage.py:4:39: W0511: TODO: move to env var before release (fixme)

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Your code has been rated at 8.80/10 (previous run: 8.33/10, +0.47)

Complexity report:

app/tasks.py

F 36:0 complete_task - A (3)

F 45:0 get_pending_tasks - A (3)

F 62:0 find_task_by_title - A (3)

F 69:0 remove_task - A (3)

F 8:0 load_tasks - A (2)

F 54:0 average_priority - A (2)

F 77:0 calculate_discount - A (2)

F 17:0 save_tasks - A (1)

F 23:0 add_task - A (1)

app/cli.py

F 6:0 main - A (1)

app/storage.py

F 7:0 format_task_report - A (2)

F 16:0 days_until_due - A (1)

F 24:0 build_query - A (1)

Table 1: Triage table for ten findings and a diff/patch
|  # | File       | Line | Code  | Finding                                 | Severity | Fix Effort | Status |
| -: | ---------- | ---: | ----- | --------------------------------------- | -------- | ---------- | ------ |
|  1 | `tasks.py` |   11 | W1514 | File opened without specifying encoding | Low      | Low        | Open   |
|  2 | `tasks.py` |   11 | R1732 | Should use `with` for file operations   | Low      | Low        | Fixed  |
|  3 | `tasks.py` |   19 | W1514 | File opened without specifying encoding | Low      | Low        | Open   |
|  4 | `tasks.py` |   23 | W0102 | Dangerous mutable default argument      | Medium   | Low        | Fixed  |
|  5 | `tasks.py` |   62 | R1710 | Inconsistent return statements          | Medium   | Low        | Fixed  |
|  6 | `tasks.py` |   71 | C0200 | Could use `enumerate()`                 | Low      | Low        | Open   |
|  7 | `tasks.py` |   79 | R1705 | Unnecessary `else` after `return`       | Low      | Low        | Open   |
|  8 | `tasks.py` |   79 | C0121 | Unnecessary comparison with `True`      | Low      | Low        | Open   |
|  9 | `cli.py`   |    6 | C0116 | Missing function docstring              | Low      | Low        | Open   |
| 10 | `cli.py`   |    2 | W0611 | Unused `save_tasks` import              | Low      | Low        | Open   |

Table 2: Comparison between linter findings and AI code-review
| Perspective      | What it Caught                                                                                                                                  | What it Missed                                                                                                              |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **Linter**       | Syntax & anti-patterns (`W0102`, `R1710`); precise file line locations.                                                                         | Logic flaws (fragile `len()` IDs); usability bugs (case-sensitivity issues); missing validation (empty text or bad ranges). |
| **AI Assistant** | Core bugs (mutable defaults, implicit returns); contextual code review (fragile ID systems); edge-case detection (handling duplicates, casing). | Automated consistency (doesn't generate strict tool codes like `W0102` out-of-the-box).                                     

### Reflection

The AI assistant is great at finding deep logic errors, complex
multi-step problems and subtle security flaws that require understanding
of what the code is trying to do. It can predict runtime failures like
how a function handles an empty dataset or what happens when you create
and delete items back to back and catch risks that a basic syntax
checker would miss.

On the other hand the rule-based linter is good at static pattern
matching, resource management and enforcing coding standards. It quickly
catches unclosed file handles, formatting issues and clear syntax errors
that don\'t need the program to run. But since it doesn\'t understand
context it can\'t see deeper logic flaws or security risks. It\'s very
precise for structural checks but it can\'t evaluate real user
experience or data integrity.
