Hey, I'm trying to clean up my project's build log and extract only the warning messages so I can share them with my team. I have a build log file at `/home/user/project/build.log` that contains a mix of info messages, warnings, and errors from our C compiler.

I need you to do two things:

1. Extract all lines from the log that match the compiler warning pattern. A warning line looks like this:
   ```
   src/<filename>.c:<line_number>:<column_number>: warning: <message>
   ```
   Specifically, the pattern I need to match is lines where:
   - They start with `src/` followed by a filename ending in `.c`
   - Then a colon, a number (line number), a colon, a number (column number), a colon
   - Then a space, the literal word `warning:`, a space, and then the warning message text
   
   For example, this is a valid line to capture:
   ```
   src/auth.c:42:8: warning: unused variable 'token'
   ```
   But these should NOT be captured:
   ```
   src/main.c:10:5: error: undeclared identifier 'x'
   [INFO] Build started at 2024-03-15 09:00:00
   src/utils.c:88:1: note: variable declared here
   ```

2. Write all matching warning lines to `/home/user/project/warnings.txt`, preserving the original order they appear in the log. Do not add any extra text, headers, or trailing newlines beyond what grep naturally produces — just the raw matching lines, one per line.

Can you help me pull out those warnings?
