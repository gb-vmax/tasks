# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When parsing inline code blocks (backtick-enclosed text), the parser seems to be generating incorrect node types and values.

### Reproduction

```js
// Parse markdown with inline code
const markdown = 'This is `inline code` in text';
const ast = parse(markdown);

// Expected: node with type "inlineCode" and the actual code value
// Actual: node has wrong type and null value
```

When I inspect the AST nodes for inline code, I'm getting unexpected results. The node type appears to be wrong and the value field is not being set correctly.

### Expected behavior

Inline code blocks should be parsed as `inlineCode` nodes with the proper string value containing the code content. The value should never be null for valid inline code.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This is breaking our markdown rendering pipeline. Any help would be appreciated!

---
Repository: /testbed
