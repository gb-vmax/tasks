# Bug Report

### Describe the bug

I'm encountering an issue with parsing blank line endings in MDX content. When a document ends with a blank line followed by EOF (null character), the parser seems to be exiting the "lineEndingBlank" state in the wrong order, which causes unexpected behavior.

### Reproduction

```js
// Parse MDX content that ends with a blank line
const content = `
# Hello

Some content

`;

// The parser doesn't handle the blank line ending correctly
// when it encounters EOF after the blank line
```

### Expected behavior

The parser should properly handle blank line endings even when they're followed by EOF. The state transitions should exit "lineEndingBlank" after consuming the null character, not before.

### Additional context

This seems to be related to the flow initialization logic in the MDX parser. The issue appears when processing documents that have trailing blank lines before the end of file marker.

---
Repository: /testbed
