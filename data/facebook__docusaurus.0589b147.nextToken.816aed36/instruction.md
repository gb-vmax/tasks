# Bug Report

### Describe the bug

I'm encountering an issue where MDX parsing fails at the end of input. It seems like the parser is not correctly detecting the end-of-file condition, which causes it to attempt reading beyond the input boundary.

### Reproduction

```js
const input = "# Hello World";
const parser = createMdxParser();

// Parser tries to read past the end of input
const result = parser.parse(input);
// Expected: successful parse
// Actual: parser attempts to access position beyond input.length
```

This happens consistently when the input ends without trailing whitespace or newlines. The parser appears to be checking for EOF incorrectly.

### Expected behavior

The parser should correctly identify when it has reached the end of the input string and return an EOF token without attempting to read beyond `input.length`.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
