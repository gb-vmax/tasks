# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX processor where the output tree is not being returned correctly. When processing MDX content, the resulting tree appears to be unexpectedly modified or incorrect.

### Reproduction

```js
const processor = createProcessor();
const tree = {
  type: 'root',
  children: [/* some content */]
};

const result = await processor.run(tree);
// result is not what I expected - seems like the tree logic changed
```

When I process an MDX file and the transformer returns an `outputTree`, the final result doesn't match what I expect. It seems like there's an issue with how the output tree is being selected or merged with the original tree.

### Expected behavior

The processor should return the transformed output tree when transformers complete successfully. If a transformer provides an `outputTree`, that should be used as the result. Otherwise, it should fall back to the original tree.

### Additional context

This might be related to how the processor handles the tree merging logic in the `run` method. The behavior seems inconsistent with previous versions.

---
Repository: /testbed
