# Bug Report

### Describe the bug

I'm experiencing an issue with MDX compilation when source maps are disabled. The compiler is returning an unexpected object structure instead of a plain string when `SourceMapGenerator` is not provided.

### Reproduction

```js
// When compiling MDX without source map support
const result = compile('# Hello', {
  // SourceMapGenerator not provided
});

// Expected: result should be a string
// Actual: result is an object with { value: string, map: undefined }
```

The compilation works fine when `SourceMapGenerator` is provided, but breaks when it's omitted or set to undefined.

### Expected behavior

When source maps are disabled (no `SourceMapGenerator`), the compiler should return a plain string value, not an object. This is how it worked before and is the expected behavior based on the API design.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
