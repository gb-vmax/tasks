# Bug Report

### Describe the bug

I'm experiencing an issue where keyword tokens in the MDX parser are not being reused correctly. When the same keyword is referenced multiple times, it seems like different token instances are being used instead of the same cached instance.

### Reproduction

```js
// When creating keyword tokens
const token1 = kw('import');
const token2 = kw('import');

// These should be the same instance from the keywords cache
console.log(token1 === token2); // Expected: true, Actual: false
```

This affects keyword token comparison and potentially impacts parser performance since tokens aren't being properly cached.

### Expected behavior

The `kw()` function should return the same TokenType instance for the same keyword name, utilizing the `keywords` cache object. Multiple calls with the same keyword should return identical references.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
