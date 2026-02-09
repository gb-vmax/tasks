# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching when using `createAbsoluteFilePathMatcher`. Files that should be matched based on glob patterns are not being detected correctly, especially when dealing with paths on different operating systems.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/home/user/docs']
);

// On Windows or when path separators don't match exactly
const result = matcher('/home/user/docs/README.md');
// Returns false when it should return true
```

The matcher seems to fail when the absolute file path doesn't have the exact trailing separator format that the root folder expects. This causes legitimate files within the root folders to not be matched against the glob patterns.

### Expected behavior

The matcher should correctly identify files within the specified root folders regardless of trailing slashes or path separator differences. Files that match the glob pattern and are contained within the root folders should return `true`.

### System Info
- Node version: 18.x
- OS: Mixed (Windows/Linux)

---
Repository: /testbed
