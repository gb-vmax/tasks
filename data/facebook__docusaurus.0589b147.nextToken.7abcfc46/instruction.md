# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where the parser seems to hang or fail to properly terminate when processing input. The tokenizer appears to not be handling end-of-file conditions correctly, which causes parsing to either continue past the input boundary or not return the expected EOF token.

### Reproduction

```js
const input = "some mdx content";
// Parser processes input but doesn't properly detect end of input
// Expected to return EOF token when pos >= input.length
// Instead continues processing or returns unexpected results
```

This seems to happen specifically when the position reaches exactly the length of the input string. The parser should recognize this as end-of-file but doesn't handle it properly.

### Expected behavior

The parser should correctly identify when it has reached the end of the input and return an EOF token. When `pos` equals `input.length`, we're at the end of the string and should finish with an EOF token.

### Additional context

This appears to be related to the tokenizer's boundary checking logic. The issue manifests when parsing completes and the position pointer is at the exact end of the input string.

---
Repository: /testbed
