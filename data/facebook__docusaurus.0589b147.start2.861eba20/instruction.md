# Bug Report

### Describe the bug

MDX expression parsing is broken - the parser seems to exit immediately after entering an expression marker instead of continuing to parse the expression content. This causes expressions to be truncated or not parsed at all.

### Reproduction

```js
// Try parsing MDX with an expression
const mdx = `
# Hello

{someVariable}

More content here
`

// The expression {someVariable} is not being parsed correctly
// Parser exits too early after consuming the opening brace
```

### Expected behavior

The parser should:
1. Enter the expression type
2. Enter and exit the marker type for the opening brace
3. Continue parsing the expression content
4. Exit the expression type after the closing brace

Currently it appears to be exiting the expression type prematurely right after consuming the opening marker, before any expression content is parsed.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
