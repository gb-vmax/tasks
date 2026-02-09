# Bug Report

### Describe the bug

I'm experiencing an issue where the MDX parser seems to be accessing array elements beyond the valid range. This appears to be causing undefined behavior when processing syntax extensions.

### Reproduction

```js
const extensions = [
  { /* extension 1 */ },
  { /* extension 2 */ },
  { /* extension 3 */ }
];

// When combining extensions, an extra iteration occurs
// This attempts to access extensions[3] which is undefined
const combined = combineExtensions(extensions);
```

### Expected behavior

The function should only iterate through the valid indices of the extensions array (0 to length-1). Currently it seems to be iterating one element past the end of the array, which could cause `syntaxExtension` to be called with `undefined` as an argument.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
