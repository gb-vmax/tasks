# Bug Report

### Describe the bug

After a recent update, markdown parsing seems to be broken for certain GFM (GitHub Flavored Markdown) syntax. I'm getting errors when trying to parse markdown content that includes specific whitespace patterns, particularly around tables and other GFM features.

### Reproduction

```js
const markdown = `
| Header 1 | Header 2 |
|----------|----------|
| Cell 1   | Cell 2   |
`;

// Parser fails or produces incorrect output
const result = parseMarkdown(markdown);
```

When trying to parse markdown with tables or other GFM syntax that involves specific spacing, the parser either throws an error or produces malformed output. This was working fine in previous versions.

### Expected behavior

The markdown parser should correctly handle whitespace in GFM syntax elements like tables, task lists, and strikethrough text. The output should match the expected AST structure for these elements.

### Additional context

This seems to affect specifically the whitespace handling in the tokenizer. Regular markdown without GFM features appears to work fine, but anything using GFM extensions has issues.

---
Repository: /testbed
