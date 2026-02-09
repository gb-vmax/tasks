# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing when processing documents that end with blank lines followed by EOF. The parser seems to be exiting the "lineEndingBlank" state prematurely when it encounters a null code, which causes unexpected behavior in the token stream.

### Reproduction

```js
const mdx = `
# Hello

Some content here

`; // Document ends with blank lines

// Parse the MDX
const result = compile(mdx);
```

When the document ends with blank lines followed by EOF (null code), the parser doesn't properly exit the "lineEndingBlank" state before consuming the null code. This results in an inconsistent token structure.

### Expected behavior

The parser should properly exit the "lineEndingBlank" state and reset the current construct before consuming the EOF marker, maintaining a consistent token structure regardless of whether the document ends with blank lines or not.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node.js version: Latest

---
Repository: /testbed
