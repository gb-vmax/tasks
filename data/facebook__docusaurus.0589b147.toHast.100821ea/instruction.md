# Bug Report

### Describe the bug

I'm experiencing an issue with markdown to HTML conversion where the output structure is incorrect when processing certain documents. The converted result seems to have malformed node structures, particularly when dealing with root-level content.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'Hello' }] }
  ]
};

const result = toHast(tree);
// Expected: proper root node with children array
// Actual: children property contains a single node object instead of array
```

When converting markdown trees, the resulting HAST structure doesn't properly wrap content in arrays when it should. This causes downstream processors to fail since they expect `children` to always be an array.

### Expected behavior

The `children` property of the root node should always contain an array of child nodes, not a single node object. Additionally, when footnotes are present, they should be properly separated with newline text nodes.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
