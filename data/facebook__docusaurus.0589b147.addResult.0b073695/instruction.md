# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where constructs with `resolveAll` are not being properly registered, and the event resolution seems to be off by one position.

### Reproduction

```js
// Create a tokenizer with a construct that has resolveAll
const construct = {
  resolveAll: (events) => {
    // This should be called but isn't
    return events;
  },
  resolve: (events) => {
    return events;
  }
};

// When the tokenizer processes events, the resolveAll function
// is never added to the resolveAllConstructs array even though
// it should be
```

### Expected behavior

1. When a construct has a `resolveAll` property, it should be added to the `resolveAllConstructs` array (currently it only gets added if it's already in the array, which doesn't make sense)
2. The `splice` operation in the resolve step should use the correct index position

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like it might be causing parsing issues with certain MDX constructs that rely on resolveAll callbacks.

---
Repository: /testbed
