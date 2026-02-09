# Bug Report

### Describe the bug

After a recent update, GFM (GitHub Flavored Markdown) parsing seems to be broken. Specifically, footnotes are no longer being recognized or rendered correctly in markdown documents.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`;

// Parse the markdown with remark-gfm
const result = parseMarkdown(markdown);

// Footnotes are not being processed
console.log(result); // footnote syntax appears as plain text
```

### Expected behavior

Footnotes should be parsed and converted into proper footnote elements. The `[^1]` reference should link to the footnote definition, and the footnote content should be rendered separately.

### Additional context

This was working fine in previous versions. It seems like footnote support might have been accidentally removed or disabled. Other GFM features like tables and strikethrough still work correctly.

---
Repository: /testbed
