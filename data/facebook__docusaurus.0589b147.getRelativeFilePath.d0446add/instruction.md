# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching in Docusaurus where absolute file paths are not being matched correctly against glob patterns. The matcher seems to be comparing paths in the wrong direction, causing files that should match to be excluded.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/path/to/docs']
);

// This should return true but returns false
const result = matcher('/path/to/docs/intro.md');
```

When I try to match files within a root folder, the matcher fails to recognize valid files. It appears that the path comparison logic is reversed - instead of checking if the absolute file path starts with the root folder path, it's checking if the root folder path ends with the absolute file path, which doesn't make sense.

### Expected behavior

The matcher should correctly identify when an absolute file path is contained within one of the specified root folders and match it against the provided glob patterns.

### Additional context

This is breaking file discovery in my Docusaurus project. Files that should be included based on the glob patterns are being skipped, and I'm getting errors about files not being contained in root folders even though they clearly are.

---
Repository: /testbed
