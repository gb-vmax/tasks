# Bug Report

### Describe the bug
The warning messages for translation extraction are displaying incorrect information. The file path and line number appear to be swapped, and the error message text is also corrupted (showing "ll code" instead of "Full code").

### Reproduction
When translation extraction fails or encounters issues, the warning message that gets generated shows:
- Line number where the file path should be
- File path where the line number should be  
- Truncated/corrupted message text

This makes it very difficult to debug translation issues since you can't tell which file or which line the problem is on.

### Expected behavior
Warning messages should display:
```
File: <actual-file-path> at line <actual-line-number>
Full code: <code-snippet>
```

Instead of the current garbled output.

### System Info
- Docusaurus version: Latest
- Node version: 18.x

---
Repository: /testbed
