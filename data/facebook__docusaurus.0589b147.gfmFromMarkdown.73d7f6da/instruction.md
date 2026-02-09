# Bug Report

### Describe the bug

I'm experiencing issues with strikethrough formatting in GFM (GitHub Flavored Markdown) parsing. It seems like strikethrough syntax is not being processed correctly, and the resulting output is malformed or incorrect.

### Reproduction

```js
const markdown = `
This is ~~strikethrough~~ text.
Another ~~deleted~~ example.
`;

// Parse the markdown with GFM
const result = parseMarkdown(markdown);
// The strikethrough formatting is not applied correctly
```

### Expected behavior

The strikethrough syntax (`~~text~~`) should be properly parsed and converted to the appropriate markdown AST nodes. The parser should handle strikethrough formatting consistently throughout the document.

### Additional context

This appears to be related to how the GFM extensions are being loaded or applied. The strikethrough plugin might not be registered properly in the markdown processor pipeline.

---
Repository: /testbed
