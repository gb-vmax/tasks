# Bug Report

### Describe the bug

I'm encountering an issue with the `serializeChunks` function in the remark-mdx vendor code. When processing chunks that contain tab characters (represented by `-2`), the output appears to be incorrect or incomplete. The serialization seems to be accessing elements beyond the array bounds and the tab tracking logic isn't working as expected.

### Reproduction

```js
const chunks = ['hello', -2, 'world', -1];
const result = serializeChunks(chunks);
// Expected: properly serialized string with tab character
// Actual: incorrect output or array access error
```

When calling `serializeChunks` with an array containing special character codes (like `-2` for tabs), the function produces unexpected results. It seems like the loop condition and the `atTab` flag handling might be causing issues.

### Expected behavior

The function should correctly serialize all chunks in the array, properly handle tab characters (code `-2`), and maintain the correct state of the `atTab` flag throughout the iteration. The loop should only process valid array indices.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
