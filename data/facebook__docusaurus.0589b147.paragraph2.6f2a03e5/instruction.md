# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where paragraphs are not being rendered correctly. When I try to parse markdown content that contains paragraph elements, the output seems malformed or incomplete.

### Reproduction

```js
const markdown = `
This is a paragraph.

This is another paragraph.
`;

const result = parseMarkdown(markdown);
console.log(result);
// Expected: proper paragraph nodes with type "paragraph"
// Actual: nodes have incorrect type or structure
```

When parsing simple markdown with multiple paragraphs, the resulting AST doesn't match what I'd expect. The paragraph nodes seem to have the wrong structure.

### Expected behavior

Paragraph nodes in the AST should have:
- `type: "paragraph"`
- `children: []` (an empty array for child nodes)

Instead, I'm seeing unexpected values for these properties.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
