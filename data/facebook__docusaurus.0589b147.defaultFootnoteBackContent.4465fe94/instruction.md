# Bug Report

### Describe the bug

The footnote back reference arrow (↩) is not appearing for the first reference of a footnote. When a footnote is referenced only once in a document, the back link at the bottom of the page is missing the arrow character entirely.

### Reproduction

```js
// Create a document with a single footnote reference
const mdx = `
Here is some text with a footnote[^1].

[^1]: This is the footnote content.
`

// Process the MDX
// Expected: The footnote back link should show "↩"
// Actual: The back link is empty/missing the arrow
```

The arrow only appears when a footnote is referenced multiple times (2 or more times). For footnotes referenced once, the back link element exists but contains no visible arrow character.

### Expected behavior

Every footnote back reference should display the ↩ arrow character, regardless of how many times the footnote is referenced in the document. The first reference should show just "↩", and subsequent references should show "↩" with a superscript number.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
