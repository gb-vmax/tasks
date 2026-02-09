# Bug Report

### Describe the bug

I'm encountering an issue with the rehype-stringify vendor module where custom node handlers are not being called correctly. When processing a tree with nodes that have registered handlers, the wrong handler (or no handler) gets invoked.

### Reproduction

```js
const processor = unified()
  .use(rehypeStringify, {
    handlers: {
      myCustomNode: (node) => {
        return '<custom>' + node.value + '</custom>'
      }
    }
  })

const tree = {
  type: 'root',
  children: [
    {
      type: 'myCustomNode',
      value: 'test content'
    }
  ]
}

const result = processor.stringify(tree)
// Expected: custom handler to be called
// Actual: handler is not invoked or wrong handler is used
```

### Expected behavior

When a node type matches a registered handler in the handlers object, that specific handler should be called to process the node. The custom handler should be invoked for nodes with matching types.

### System Info
- rehype-stringify version: 10.0.0
- Node version: 18.x

---
Repository: /testbed
