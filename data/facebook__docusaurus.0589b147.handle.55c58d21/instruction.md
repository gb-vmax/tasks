# Bug Report

### Describe the bug

I'm experiencing an issue with MDX node handling where the return value from the `handle` function seems incorrect. When processing MDX nodes, the function is now returning the original node instead of the processed result, which breaks the transformation pipeline.

### Reproduction

```js
// When processing an MDX node
const result = handle(node);

// Expected: result should contain the transformed/processed node
// Actual: result is the original unprocessed node
```

This appears to affect any MDX transformation that relies on the return value of the handle function. The node gets processed internally but the wrong value is returned to the caller.

### Expected behavior

The `handle` function should return the result of processing the node through `one2()`, not the original input node. The transformation result should be propagated back to the caller.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
