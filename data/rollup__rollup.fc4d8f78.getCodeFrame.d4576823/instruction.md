# Bug Report

### Describe the bug

The code frame display is showing the wrong line highlighted when an error occurs. The error indicator (usually an arrow or highlighting) appears on the line above where the actual error is located, making it confusing to identify the exact source of the problem.

### Reproduction

When an error occurs in the code, the generated code frame highlights the wrong line. For example, if there's a syntax error on line 5, the code frame shows the error marker on line 4 instead.

This makes debugging harder because you have to mentally adjust which line the error is actually on.

### Expected behavior

The code frame should highlight the exact line where the error occurred. If the error is reported on line 5, line 5 should be marked as the error line in the output, not line 4.

### Additional context

This seems to have started recently. The line numbers shown in the frame are correct, but the highlighting/arrow is off by one line.

---
Repository: /testbed
