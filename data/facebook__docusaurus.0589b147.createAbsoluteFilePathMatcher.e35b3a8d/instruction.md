# Bug Report

### Describe the bug

File path matching is broken on Windows when using `createAbsoluteFilePathMatcher`. The function fails to correctly identify files within root folders because it's not properly handling path separators.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['C:\\Users\\project\\docs'],
  ['**/*.md']
);

// This fails on Windows
const filePath = 'C:\\Users\\project\\docs\\intro.md';
// Error: File path does not belong to any of the root folders
```

### Expected behavior

The matcher should correctly identify that `C:\Users\project\docs\intro.md` belongs to the root folder `C:\Users\project\docs` and process it accordingly. The path matching should work consistently across different operating systems.

### System Info
- OS: Windows 10
- Node version: 18.x

---
Repository: /testbed
