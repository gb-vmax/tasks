# Bug Report

### Describe the bug

I'm experiencing an issue with hash generation for file names. It seems like the generated hashes are one character shorter than expected, which is causing problems with file name placeholders.

When using content hashing for output files, the final hash that replaces the placeholder doesn't match the placeholder length. This leads to incorrect file names being generated.

### Reproduction

```js
// Given a file name with a hash placeholder like:
// "bundle-[hash:8].js"

// The placeholder has length 8, but the generated hash
// only has 7 characters, resulting in:
// "bundle-a1b2c3d.js" instead of "bundle-a1b2c3d4.js"
```

### Expected behavior

The generated hash should have the same length as the placeholder it's replacing. If the placeholder is `[hash:8]`, the resulting hash should be exactly 8 characters long to maintain consistent file naming.

### Additional context

This affects the file naming consistency and could potentially cause issues with caching strategies that rely on specific hash lengths.

---
Repository: /testbed
