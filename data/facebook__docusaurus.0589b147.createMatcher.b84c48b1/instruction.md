# Bug Report

### Describe the bug

I'm experiencing an issue with pattern matching where the behavior seems completely inverted. When I provide patterns to match against, files that should be excluded are being included, and files that should be included are being excluded.

### Reproduction

```js
const matcher = createMatcher(['*.md', '*.txt']);

// This returns false but should return true
matcher('README.md');

// This returns true but should return false  
matcher('index.js');
```

Also, when passing an empty array of patterns, it seems to match everything instead of nothing:

```js
const emptyMatcher = createMatcher([]);

// This returns true but should return false
emptyMatcher('any-file.txt');
```

### Expected behavior

- Files matching the provided patterns should return `true`
- Files not matching the patterns should return `false`
- When no patterns are provided, nothing should match (return `false` for all inputs)

### System Info
- docusaurus-utils version: latest
- Node: v18.x

---
Repository: /testbed
