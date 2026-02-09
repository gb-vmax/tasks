# Bug Report

### Describe the bug

When converting markdown AST nodes to markdown strings, text nodes are not being properly escaped. Special characters and markdown syntax in text content are being rendered literally instead of being escaped, which breaks the markdown output.

### Reproduction

```js
const mdast = {
  type: 'text',
  value: 'This has *asterisks* and [brackets]'
}

// Convert to markdown
const result = toMarkdown(mdast)

// Expected: 'This has \\*asterisks\\* and \\[brackets\\]'
// Actual: 'This has *asterisks* and [brackets]'
```

When text contains markdown special characters like `*`, `_`, `[`, `]`, etc., they should be escaped in the output. Currently they're being passed through unescaped, which causes them to be interpreted as markdown syntax instead of literal text.

### Expected behavior

Text nodes should have their special characters properly escaped when converting to markdown format. The `safe` method should be used to escape the content before returning it.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
