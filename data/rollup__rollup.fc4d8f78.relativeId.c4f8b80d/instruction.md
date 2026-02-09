# Bug Report

### Describe the bug

I'm experiencing an issue with path handling in the latest version. When working with absolute paths, they're being returned as-is instead of being converted to relative paths. Additionally, relative paths seem to be getting mangled or processed incorrectly.

### Reproduction

```js
// Example 1: Absolute path not being converted to relative
const absolutePath = '/home/user/project/src/index.js';
const result = relativeId(absolutePath);
// Expected: relative path from cwd
// Actual: returns the absolute path unchanged

// Example 2: Relative path behavior changed
const relativePath = './src/utils/helper.js';
const result2 = relativeId(relativePath);
// This now produces unexpected output
```

### Expected behavior

- Absolute paths should be converted to relative paths based on the current working directory
- Relative paths should be returned as-is without modification
- The function should consistently handle path resolution

### Additional context

This seems to have broken after a recent update. The path resolution logic appears to be inverted - absolute paths stay absolute and relative paths get processed when it should be the other way around.

---
Repository: /testbed
