# Bug Report

### Bug: Code frame showing incorrect line range in error messages

I've noticed that error messages with code frames are displaying the wrong lines from the source code. The frame seems to be off by one line when showing context around the error location.

### Reproduction

When an error occurs at a specific line, the code frame that's displayed includes one extra line at the bottom that shouldn't be there. For example, if an error is on line 10, the frame shows lines 7-13 instead of the expected 7-12.

This also affects the logic for trimming empty lines at the end of the frame - it's checking and removing the wrong line, which can leave trailing whitespace or remove lines that should be displayed.

### Expected behavior

The code frame should show:
- 3 lines before the error line
- The error line itself
- 2 lines after the error line

So for an error on line 10, it should display lines 7-12, not 7-13.

The trimming of empty trailing lines should also work correctly and not accidentally remove content lines or leave empty ones.

### Additional context

This appears to affect all error reporting where code frames are generated, making it harder to understand the context of errors since the displayed range doesn't match what's expected.

---
Repository: /testbed
