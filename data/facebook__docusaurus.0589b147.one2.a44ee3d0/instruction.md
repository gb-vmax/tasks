# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where custom node handlers are being called even when they don't exist, leading to errors. Additionally, nodes that should be passed through are being incorrectly filtered.

### Reproduction

When processing MDX content with custom handlers and passThrough options:

```js
const processor = createProcessor({
  handlers: {
    customNode: myHandler
  },
  passThrough: ['html', 'jsx']
});

// Processing fails when encountering nodes without handlers
// Also, nodes in passThrough list are not being passed through correctly
```

The processor throws errors when it encounters node types that have no handler defined, even though the handler check should prevent this. Also, nodes specified in the `passThrough` array are being incorrectly processed instead of being passed through.

### Expected behavior

- Nodes without handlers should fall through to the unknown handler or default behavior
- Nodes specified in `passThrough` should be passed through without modification
- No errors should be thrown for missing handlers when the handler existence check fails

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a logic error in the node processing conditions. The behavior changed recently and is causing issues with custom MDX transformations.

---
Repository: /testbed
