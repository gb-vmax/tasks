# Bug Report

### Describe the bug

I'm experiencing an issue with the `safe` function binding in the remark stringify module. When using the `safeBound` function, it appears that the context (`this`) is not being passed correctly to the underlying `safe` function, which is causing unexpected behavior in markdown serialization.

### Reproduction

```js
const processor = remark();
const ast = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'some text with special chars' }
  ]
};

// When stringifying with special characters
const result = processor.stringify(ast);
// The safe function context is incorrect
```

The issue seems to be related to how `safeBound` is calling the `safe` function. The arguments are being passed in the wrong order or the context binding is incorrect.

### Expected behavior

The `safeBound` function should correctly pass the context and arguments to the `safe` function so that markdown special characters are properly escaped during serialization.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
