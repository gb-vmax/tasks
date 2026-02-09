# Bug Report

### Describe the bug

I'm encountering an issue with the `stringify` method in the Processor class. When I try to stringify a tree, I'm getting unexpected behavior - it seems like the arguments being passed to the compiler are in the wrong order.

### Reproduction

```js
const processor = new Processor();
const tree = {
  type: 'root',
  children: [/* ... */]
};
const file = vfile('example.md');

// This produces incorrect output
const result = processor.stringify(tree, file);
```

### Expected behavior

The compiler should receive the tree as the first argument and the file as the second argument, allowing it to properly stringify the AST. Instead, it appears the arguments are being passed in reverse order, causing the compiler to fail or produce incorrect results.

Also noticed that `freeze()` is being called on the tree object instead of the processor instance, which doesn't make sense since trees don't have a freeze method.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
