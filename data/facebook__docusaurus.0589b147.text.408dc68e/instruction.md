# Bug Report

### Describe the bug

I'm experiencing an issue with text node conversion in the markdown-to-HTML transformation. When converting markdown text nodes to HAST (HTML AST), the resulting output is incorrect - instead of getting a proper text node object, I'm getting a string value returned directly.

### Reproduction

```js
const mdast = {
  type: 'text',
  value: '  Hello World  '
};

const state = {
  patch: (node, result) => {},
  applyData: (node, result) => result
};

const result = text(state, mdast);
// Expected: { type: 'text', value: 'Hello World' }
// Actual: 'Hello World' (just a string)
```

### Expected behavior

The `text()` handler should return a proper HAST text node object with `type: "text"` and a `value` property, not just a raw string. The return value should be a node object that can be properly integrated into the HAST tree structure.

### Additional context

This seems to have broken after a recent change. The function is now returning the result of `trimLines()` directly instead of returning the node object. This breaks any code that expects a proper node structure from the text handler.

---
Repository: /testbed
