# Bug Report

### Describe the bug

The `run()` method is resolving the promise with the original tree before transformers have been applied, causing the returned tree to not include any transformations. Additionally, when using the callback-style API, the arguments passed to the callback appear to be in the wrong order.

### Reproduction

```js
const processor = unified()
  .use(someTransformerPlugin)
  .use(anotherTransformerPlugin);

const tree = {
  type: 'root',
  children: []
};

// Promise-based API returns untransformed tree
const result = await processor.run(tree);
// result is the original tree, not the transformed one

// Callback-based API receives arguments in unexpected order
processor.run(tree, (error, transformedTree, file) => {
  // transformedTree and file seem to be swapped
});
```

### Expected behavior

The promise should resolve with the fully transformed tree after all transformers have been applied, not the original input tree. The callback should receive arguments in the documented order: `(error, tree, file)`.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
