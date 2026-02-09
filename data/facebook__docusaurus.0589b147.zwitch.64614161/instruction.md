# Bug Report

### Describe the bug
When using the rehype-stringify vendor module, handlers are not being correctly resolved for certain node types. The handler lookup appears to be checking the wrong object for the handler key, which causes valid handlers to be skipped and potentially triggers the invalid handler callback unexpectedly.

### Reproduction
```js
const handlers = {
  'element': (node) => { /* handle element */ },
  'text': (node) => { /* handle text */ }
};

const processor = {
  handlers: handlers,
  invalid: (node) => console.log('Invalid node type'),
  unknown: (node) => console.log('Unknown handler')
};

// When processing a node with type 'element'
const node = {
  type: 'element',
  tagName: 'div'
};

// The handler lookup fails even though 'element' exists in handlers
// Falls through to invalid callback instead of using the correct handler
```

### Expected behavior
The processor should correctly look up handlers from the `handlers` object based on the node's type/key property. Valid handlers should be called when they exist, and only fall back to `unknown` or `invalid` handlers when appropriate.

### System Info
- rehype-stringify version: 10.0.0
- Node.js version: Latest

This seems to have broken handler resolution entirely. Any help would be appreciated!

---
Repository: /testbed
