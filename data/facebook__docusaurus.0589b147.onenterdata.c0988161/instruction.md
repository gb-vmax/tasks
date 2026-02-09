# Bug Report

### Describe the bug

I'm experiencing a crash when parsing MDX content with text nodes. The parser seems to be accessing the wrong element in the stack, which causes it to fail when trying to read properties from `undefined`.

### Reproduction

```js
// Parse any MDX content with regular text
const result = compile('Hello world');
```

When the parser encounters text data, it tries to access `node2.children` but `node2` is undefined because the stack index is off by one. This results in a "Cannot read property 'children' of undefined" error.

### Expected behavior

The parser should correctly handle text nodes without crashing. Text content should be parsed and added to the appropriate parent node in the AST.

### Additional context

This appears to happen consistently with any MDX content that contains plain text. The issue seems related to how the parser manages its internal stack when entering text data nodes.

---
Repository: /testbed
