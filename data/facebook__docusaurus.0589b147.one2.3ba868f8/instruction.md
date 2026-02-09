# Bug Report

### Describe the bug

I'm experiencing an issue with MDX processing where custom handlers aren't being invoked properly. When I define a custom handler for a specific node type, it seems to be ignored and the default/unknown handler is called instead.

### Reproduction

```js
const mdx = require('@mdx-js/mdx');

const customHandler = (state, node, parent) => {
  // Custom logic here
  return { type: 'custom', value: 'processed' };
};

const result = await mdx.compile(content, {
  remarkPlugins: [
    () => (tree) => {
      // Register custom handler
      tree.handlers = {
        myCustomType: customHandler
      };
    }
  ]
});

// Expected: custom handler to be called
// Actual: unknown handler is called instead
```

When processing nodes with registered handlers, the custom handler function is completely bypassed and the unknownHandler gets invoked. This breaks custom node processing logic that was working before.

### Expected behavior

When a handler is registered for a specific node type, that handler should be called when processing nodes of that type. The custom handler should have priority over the unknown/default handler.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
