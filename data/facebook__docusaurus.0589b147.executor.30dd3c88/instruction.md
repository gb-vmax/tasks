# Bug Report

### Describe the bug

I'm encountering an issue with the MDX processor where the promise-based API doesn't seem to be resolving correctly. When using the processor with promises (without passing a callback), the resulting tree is not being returned as expected.

### Reproduction

```js
const processor = createProcessor();
const tree = { type: 'root', children: [] };

// Using promise-based API
const result = await processor.run(tree);
// result is undefined instead of the processed tree
```

### Expected behavior

When using the promise-based API (without a callback), the processor should resolve with the processed tree. The promise should return the resulting tree after transformations are applied.

### Additional context

This appears to affect cases where the processor is used without a callback function. The callback-based API might still work correctly, but the promise-based approach returns unexpected results.

---
Repository: /testbed
