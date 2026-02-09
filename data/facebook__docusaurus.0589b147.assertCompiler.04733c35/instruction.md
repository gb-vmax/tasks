# Bug Report

### Describe the bug

I'm getting a `TypeError` when trying to use the compiler functionality. The error message says "Cannot use `[method name]` with `compiler`" even though I'm providing a valid compiler function.

### Reproduction

```js
const processor = remark()
  .use(somePlugin)
  .data('compiler', myCompilerFunction);

// Throws: TypeError: Cannot use `stringify` with `compiler`
const result = processor.stringify(tree);
```

The compiler is a proper function but it's being rejected. This seems backwards - it should only throw an error when the compiler is NOT a function, but instead it's throwing when it IS a function.

### Expected behavior

The processor should accept a compiler function and use it for stringifying the AST. The error should only be thrown when the compiler is missing or not a function.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
