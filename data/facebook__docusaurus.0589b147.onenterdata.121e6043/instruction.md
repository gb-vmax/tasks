# Bug Report

### Describe the bug

I'm experiencing an issue with text node handling in markdown parsing. When processing consecutive text tokens, the parser seems to be incorrectly accessing or creating text nodes, which results in malformed output or unexpected behavior.

### Reproduction

```js
const markdown = `This is some text
with multiple lines
and consecutive text tokens`;

const result = remark.parse(markdown);
// The text nodes are not being created or merged correctly
```

When parsing markdown with consecutive text content, the text nodes appear to be incorrectly positioned or duplicated in the AST. This affects the final output when converting back to markdown or HTML.

### Expected behavior

Text tokens should be properly collected into text nodes. When a new text token is encountered and the previous sibling is already a text node, it should reuse that node. When there's no existing text node or the previous sibling is a different type, a new text node should be created and added to the children array.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
