# Bug Report

### Describe the bug

I'm experiencing an issue with GFM (GitHub Flavored Markdown) footnote parsing. When using footnote references in markdown content, the parser seems to be accepting invalid syntax that should be rejected.

### Reproduction

```js
const markdown = `
Some text with a footnote[1] reference.

[^1]: This is the footnote content.
`;

// Parser is now accepting footnote calls without the caret (^) marker
// This should fail but doesn't anymore
const invalidMarkdown = `
Text with invalid footnote[1] without caret.
`;
```

### Expected behavior

Footnote references should require the proper syntax with a caret marker (`[^1]`). References without the caret like `[1]` should not be parsed as valid GFM footnotes.

The parser appears to have stopped validating that the caret character is present after the opening bracket in footnote calls, allowing malformed footnote syntax to pass through.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
