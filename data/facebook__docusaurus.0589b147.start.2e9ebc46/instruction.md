# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where blank lines with leading whitespace are not being handled correctly. The parser seems to be consuming the whitespace but not properly advancing to the next state.

### Reproduction

```js
const markdown = `
  
Some text after blank line with spaces
`

// Parse the markdown
const result = remark.parse(markdown)

// The blank line with leading spaces causes incorrect parsing
```

### Expected behavior

Blank lines with leading whitespace should be processed the same way as blank lines without whitespace. The parser should correctly identify the blank line and continue parsing the subsequent content.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
