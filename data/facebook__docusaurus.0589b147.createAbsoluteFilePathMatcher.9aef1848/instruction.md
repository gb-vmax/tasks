# Bug Report

### Describe the bug

I'm experiencing an issue with file path matching in Docusaurus. When using glob patterns to match files, the matcher is not correctly identifying files that should match the pattern. It seems like the absolute file paths are being passed directly to the matcher instead of being converted to relative paths first.

### Reproduction

```js
const matcher = createAbsoluteFilePathMatcher(
  ['**/*.md'],
  ['/path/to/docs']
);

// This should return true but returns false
const result = matcher('/path/to/docs/guide/intro.md');
console.log(result); // Expected: true, Actual: false
```

The glob pattern `**/*.md` should match any markdown file in the docs folder, but it's not working as expected. The file paths don't seem to be getting converted to relative paths before being matched against the glob pattern.

### Expected behavior

The matcher should convert absolute file paths to relative paths (relative to the root folder) before testing them against the glob pattern. For example, `/path/to/docs/guide/intro.md` should be converted to `guide/intro.md` and then matched against `**/*.md`, which should return true.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
