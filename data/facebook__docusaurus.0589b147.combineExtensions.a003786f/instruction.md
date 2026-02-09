# Bug Report

### Describe the bug

I'm experiencing an issue with `combineExtensions` where only the last extension in the array is being applied. When passing multiple extensions, all previous extensions are being ignored and only the final one takes effect.

### Reproduction

```js
const ext1 = {
  document: {
    91: { /* config for ext1 */ }
  }
};

const ext2 = {
  document: {
    92: { /* config for ext2 */ }
  }
};

const combined = combineExtensions([ext1, ext2]);

// Expected: combined should contain configurations from both ext1 and ext2
// Actual: combined only contains configuration from ext2
```

### Expected behavior

When combining multiple extensions, the resulting object should include all configurations from all extensions in the array. Each extension should be merged into the combined result.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
