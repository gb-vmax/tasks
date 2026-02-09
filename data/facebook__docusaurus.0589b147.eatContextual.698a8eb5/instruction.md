# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where contextual keywords are being consumed even when they don't match the expected value. This is causing the parser to incorrectly advance past tokens, leading to syntax errors in valid MDX documents.

### Reproduction

```js
// When parsing MDX with contextual keywords
// The parser incorrectly consumes tokens before validation

// Example MDX that triggers the issue:
const mdxContent = `
export const meta = {
  title: 'Example'
}

# Hello World
`

// The parser advances the token stream before checking
// if the contextual keyword matches, causing it to skip
// over valid tokens when the match fails
```

### Expected behavior

The parser should only advance to the next token after confirming that the current token matches the expected contextual keyword. If the token doesn't match, it should remain at the current position and return false without consuming the token.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken after a recent change to the tokenizer. The parser is now eating tokens it shouldn't be touching.

---
Repository: /testbed
