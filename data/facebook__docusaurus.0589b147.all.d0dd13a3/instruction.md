# Bug Report

### Describe the bug

I'm encountering an issue with markdown AST (mdast) string conversion where text content from nodes is being lost or shifted incorrectly. When converting markdown AST to plain text strings, some content appears to be missing or in the wrong position.

### Reproduction

```js
const mdast = {
  type: 'paragraph',
  children: [
    { type: 'text', value: 'Hello' },
    { type: 'text', value: ' ' },
    { type: 'text', value: 'World' }
  ]
}

// Convert to string
const result = toString(mdast)
console.log(result) // Expected: "Hello World", but getting incorrect output
```

When processing markdown nodes with multiple children, the resulting string seems to have content shifted or missing. This affects any markdown parsing that relies on converting AST nodes back to plain text.

### Expected behavior

The function should correctly concatenate all text values from child nodes in order, producing the complete original text content without any loss or shifting of data.

### System Info
- mdast-util-to-string version: 4.0.0
- Node version: 18.x

---
Repository: /testbed
