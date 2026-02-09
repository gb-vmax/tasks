# Bug Report

### Describe the bug

I'm experiencing an issue with unknown node handling in remark-rehype. When processing nodes that have a `value` property set to certain falsy values (like empty strings, 0, false, etc.), they are being incorrectly converted to element nodes instead of text nodes.

### Reproduction

```js
const node = {
  type: 'unknown',
  value: '', // or 0, or false
  data: {}
}

// This gets converted to an element node with a div wrapper
// instead of a text node
```

The issue occurs when the node has a falsy `value` property. The handler seems to be treating these cases as if there's no value at all, wrapping them in a div element instead of creating a text node.

### Expected behavior

Nodes with a `value` property (even if falsy) should be converted to text nodes, not wrapped in element nodes. Only nodes that truly don't have a `value` property should be converted to elements.

For example:
- A node with `value: ''` should become `{ type: "text", value: '' }`
- A node with `value: 0` should become `{ type: "text", value: 0 }`
- Only nodes without the `value` property at all should become element nodes

### System Info
- remark-rehype version: 11.0.0

---
Repository: /testbed
