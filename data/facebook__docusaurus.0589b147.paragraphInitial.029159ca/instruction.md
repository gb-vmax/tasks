# Bug Report

### Describe the bug

When parsing MDX content with paragraphs, the token type being emitted is incorrect. Instead of entering a "paragraph" token at the start of a paragraph, the parser is entering a "paragraphContinuation" token, which breaks the expected AST structure.

### Reproduction

```js
const mdx = `
This is a paragraph.

Another paragraph here.
`;

// Parse the MDX content
const result = compile(mdx);
// The AST should show "paragraph" tokens but shows "paragraphContinuation" instead
```

### Expected behavior

When the parser encounters the beginning of a paragraph, it should emit a "paragraph" token type, not "paragraphContinuation". The "paragraphContinuation" token should only be used for subsequent lines within an existing paragraph.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
