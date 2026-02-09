# Bug Report

### Describe the bug

I'm encountering an issue with footnote parsing in GFM (GitHub Flavored Markdown). It seems like footnotes are not being recognized or processed correctly when parsing markdown content.

### Reproduction

When I try to parse markdown with footnotes, they're not being converted properly:

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// Footnotes are missing from the output
console.log(result); // footnote elements are not present
```

### Expected behavior

Footnotes should be parsed and included in the output AST. The footnote reference `[^1]` should be linked to its corresponding footnote definition.

### Additional context

This appears to have started happening recently. Strikethrough formatting still works fine, but footnotes are completely ignored during parsing. Not sure if this is related to a recent change in the GFM parser configuration.

---
Repository: /testbed
