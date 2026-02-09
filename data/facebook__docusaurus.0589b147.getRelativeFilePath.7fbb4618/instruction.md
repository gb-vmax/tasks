# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching in `createAbsoluteFilePathMatcher`. When trying to match files against glob patterns, the matcher is not working correctly - it seems like the logic for determining relative file paths is inverted.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/home/user/project/docs']
);

// This should match but doesn't
const result = matcher('/home/user/project/docs/intro.md');
// Expected: true
// Actual: false or throws error
```

The function appears to be checking if the root folder starts with the file path instead of the other way around, and then computing the relative path in the wrong direction.

### Expected behavior

The matcher should correctly identify when an absolute file path is within one of the specified root folders and properly calculate the relative path for pattern matching.

### System Info
- Package: @docusaurus/utils
- Node version: 18.x

---
Repository: /testbed
