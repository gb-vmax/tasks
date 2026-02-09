# Bug Report

### Describe the bug

When using MDX without source maps enabled, the compiler returns an object instead of a string value. This causes issues when trying to process the compiled output as it's expecting a string but receives an object with a `value` property.

### Reproduction

```js
// Compile MDX without SourceMapGenerator
const result = compile('# Hello', {
  // No SourceMapGenerator provided
});

// Expected: string
// Actual: object with { value: '...', map: undefined }
console.log(typeof result); // prints 'object' instead of 'string'
```

### Expected behavior

The compiler should consistently return a string value regardless of whether source maps are enabled or not. When `SourceMapGenerator` is not provided, it should return just the compiled string, not an object containing the value.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
