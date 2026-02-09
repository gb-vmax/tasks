# Bug Report

### Describe the bug

I'm experiencing an issue where error messages and warnings are showing incorrect line and column numbers in the output. The location information appears to be swapped - the line number is being displayed where the column should be, and vice versa.

### Reproduction

When I trigger an error or warning during the build process, the reported location doesn't match the actual position in the source file. For example:

```js
// Actual error location: line 42, column 15
// Reported location: line 15, column 42
```

This makes it really difficult to track down issues in the code since I have to manually figure out where the actual problem is.

### Expected behavior

The error/warning messages should display the correct line and column numbers matching the actual position in the source file. Line should show the line number and column should show the column number.

### System Info
- Version: latest
- Node: 18.x

---
Repository: /testbed
