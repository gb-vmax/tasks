# Bug Report

### Describe the bug

After a recent update, I'm noticing that the output structure from `toHast()` has changed unexpectedly. When converting markdown trees to HTML AST, the resulting tree now always includes an extra newline text node at the end, even when there's no footer content.

### Reproduction

```js
const tree = {
  type: 'root',
  children: [
    { type: 'paragraph', children: [{ type: 'text', value: 'Hello' }] }
  ]
};

const result = toHast(tree);
// Result now has an unexpected text node with "\n" at the end
```

### Expected behavior

The newline text node should only be added when there's actually footer content to separate. Without a footer, the converted tree should not have this extra newline node appended to the children array.

Previously, the newline was only inserted between the main content and the footer when a footer existed. Now it appears unconditionally, which breaks downstream processing that expects a clean tree structure without trailing whitespace nodes.

### System Info
- remark-rehype version: 11.0.0
- Node version: 18.x

---
Repository: /testbed
