# Bug Report

### Describe the bug

I'm experiencing an issue with footnote references in markdown parsing. When processing footnotes, the text content appears to be duplicated in the output. It seems like the buffer is being called twice, causing the footnote label/identifier to be repeated.

### Reproduction

```js
const markdown = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`;

// Parse the markdown
const result = parseMarkdown(markdown);

// The footnote reference identifier gets duplicated
console.log(result);
// Expected: footnote reference with label "1"
// Actual: footnote reference with label "11" or duplicated content
```

### Expected behavior

Footnote references should have their identifiers/labels processed once, not duplicated. The parser should correctly extract the footnote marker without repeating the buffered content.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
