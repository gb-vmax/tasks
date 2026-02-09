# Bug Report

### Describe the bug

I'm experiencing an issue with GFM (GitHub Flavored Markdown) parsing where footnotes are not being recognized or processed correctly. When I include footnotes in my markdown content, they're not being converted to the expected output format.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`;

// Process the markdown with remark-gfm
const result = processMarkdown(markdown);

// Footnotes are missing from the output
console.log(result);
```

### Expected behavior

Footnotes should be parsed and included in the AST/output. The footnote reference `[^1]` should be linked to its definition, and the footnote content should be rendered appropriately.

### Additional context

This seems to have started happening recently. I'm using remark-gfm@4.0.0 and footnotes were working fine before. Other GFM features like tables and strikethrough are working as expected, but footnotes specifically are not being processed.

---
Repository: /testbed
