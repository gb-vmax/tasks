# Bug Report

### Describe the bug

I'm experiencing an issue with markdown code block indentation. When converting markdown AST to string output, code blocks and other indented content are not being properly indented - they're just appearing without any indentation at all.

### Reproduction

```js
const markdown = `
# Header

    indented code block
    second line
`;

// Process the markdown through remark
const result = processor.processSync(markdown);

// The output loses the indentation:
// # Header
//
// indented code block
// second line
//
// Expected output should preserve the 4-space indentation
```

This affects any content that should be indented, including:
- Indented code blocks
- Nested lists
- Blockquotes with nested content

### Expected behavior

The markdown serializer should preserve indentation levels when converting the AST back to markdown format. Indented code blocks should maintain their leading spaces, nested list items should be properly indented, etc.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
