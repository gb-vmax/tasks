# Bug Report

### Describe the bug

I'm encountering an issue with inline code parsing in markdown. When I have inline code within other markdown elements, the code text is not being properly attached to the correct node in the AST. Instead, it seems to be getting assigned to the wrong parent node.

### Reproduction

```js
const markdown = `Some text with \`inline code\` here`;

// Parse the markdown
const result = remark().parse(markdown);

// The inline code node structure is incorrect
// The text property is being set on the wrong node level
```

When parsing markdown with inline code (backtick syntax), the resulting AST structure doesn't match what I'd expect. The code text appears to be assigned to a parent node rather than the immediate code node itself.

### Expected behavior

The inline code text should be properly stored in the correct node of the AST tree. The parser should maintain the proper parent-child relationship for inline code elements.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
