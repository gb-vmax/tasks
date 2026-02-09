# Bug Report

### Describe the bug

I'm experiencing an issue with footnote definitions not being processed correctly. When I include footnote definitions in my markdown, they don't appear in the parsed output at all. It seems like the parser is completely skipping over footnote definition blocks.

### Reproduction

```js
const markdown = `
Here is some text with a footnote reference[^1].

[^1]: This is the footnote definition.
`;

const result = parseMarkdown(markdown);
console.log(result);
// Expected: footnote definition should be in the AST
// Actual: footnote definition is missing from output
```

### Expected behavior

Footnote definitions should be parsed and included in the AST. The footnote content should be accessible in the parsed result.

### Additional context

This appears to have started recently. Previously, footnotes were working fine but now they're being silently ignored during parsing. Regular footnote references (like `[^1]`) still seem to work, but the actual definitions are not being captured.

---
Repository: /testbed
