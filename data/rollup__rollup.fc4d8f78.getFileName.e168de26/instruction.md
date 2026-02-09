# Bug Report

### Describe the bug

I'm encountering an issue with external module path resolution when using the `renormalizeRenderPath` option. The paths are being generated incorrectly - it seems like the logic is inverted.

### Reproduction

```js
// Setup with renormalizeRenderPath enabled
const options = {
  external: ['some-external-module'],
  output: {
    paths: {
      'some-external-module': './custom/path/module.js'
    }
  }
};

// When renormalizeRenderPath is true
// Expected: normalized relative path
// Actual: returns the raw module id instead

// When renormalizeRenderPath is false  
// Expected: returns the raw module id
// Actual: normalized relative path is returned
```

### Expected behavior

When `renormalizeRenderPath` is `true`, the file path should be normalized using `normalize(relative(inputBase, id))`. When it's `false`, it should just return the module `id` as-is.

Currently it appears to be doing the opposite - normalizing when the flag is false and returning the raw id when the flag is true.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
