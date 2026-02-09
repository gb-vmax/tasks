# Bug Report

### Describe the bug

I'm experiencing an issue with error reporting where the line and column numbers in error messages are swapped. When an error occurs during build, the location information points to the wrong position in the source file, making it very difficult to debug.

### Reproduction

```js
// Create a file with a syntax error at line 10, column 5
// The error message reports it as line 5, column 10 instead

// For example, if you have an error at:
// Line: 15
// Column: 8

// The error output shows:
// Line: 8
// Column: 15
```

### Expected behavior

Error messages should report the correct line and column numbers matching the actual position in the source file. If an error occurs at line 15, column 8, the error should display those exact coordinates, not swap them.

### Additional context

This seems to affect all error reporting that includes location information. The line and column values appear to be reversed in the output, which makes it really confusing when trying to locate issues in larger files.

---
Repository: /testbed
