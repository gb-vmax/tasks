# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where line and column tracking appears to be broken. After recent changes, the position tracking seems to increment incorrectly, causing the parser to lose track of where it is in the document.

### Reproduction

When parsing MDX content with line breaks, the tokenizer's position tracking gets corrupted:

```js
const mdx = `
# Heading

Some paragraph text
with multiple lines
`

// Parse the MDX content
const result = compile(mdx)
// Position information in the AST is incorrect
```

The line and column numbers in the resulting AST don't match the actual positions in the source text. This affects error reporting and source maps.

### Expected behavior

The tokenizer should correctly track line numbers and column positions as it consumes characters. Line numbers should increment only at actual line endings, and columns should reset appropriately.

### Additional context

This seems to have started happening recently. The position tracking is critical for error messages and debugging, so this is causing issues in our workflow.

---
Repository: /testbed
