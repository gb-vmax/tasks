# Bug Report

### Describe the bug

I'm experiencing an issue with the `combineExtensions` function in the remark-gfm vendor file. When multiple extensions are passed to be combined, only the last extension in the array seems to be retained, and all previous extensions are lost.

### Reproduction

```js
const ext1 = { feature1: { /* config */ } };
const ext2 = { feature2: { /* config */ } };
const ext3 = { feature3: { /* config */ } };

const combined = combineExtensions([ext1, ext2, ext3]);

// Expected: combined should contain feature1, feature2, and feature3
// Actual: combined only contains feature3
console.log(combined); // Only shows feature3
```

### Expected behavior

When combining multiple extensions, the resulting object should contain all features from all extensions merged together. Each extension should add to the combined result, not replace it.

### System Info
- remark-gfm version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
