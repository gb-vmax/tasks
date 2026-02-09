# Bug Report

### Describe the bug

I'm experiencing an issue with translation extraction warnings where the reported line numbers in error messages are incorrect. When there's a translation issue in my source code, the warning message points to the wrong line number, making it very difficult to locate the actual problem.

### Reproduction

1. Create a source file with translation calls
2. Introduce a translation issue (e.g., missing translation key)
3. Run the translation extraction process
4. Check the warning message output

The warning message shows the ending line number instead of the starting line number where the translation call actually begins. For files with multi-line translation calls, this makes debugging confusing since the reported line doesn't match where the issue originates.

### Expected behavior

The warning message should report the line number where the translation call starts (the opening line), not where it ends. This would make it much easier to locate and fix translation issues in the source code.

Example of what I'm seeing:
```
File: src/pages/index.js at line 15
```

When the actual translation call starts at line 10 but ends at line 15.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
