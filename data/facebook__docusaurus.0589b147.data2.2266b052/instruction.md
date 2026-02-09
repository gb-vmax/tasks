# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where line breaks in text content are being consumed incorrectly. When text data contains line breaks, the parser seems to be consuming the break character at the wrong point in the tokenization process, which causes the output to be malformed.

### Reproduction

```mdx
This is some text content
with a line break in the middle
and it should be preserved correctly
```

When parsing MDX content with line breaks, the break characters appear to be getting consumed before the data token is properly exited, leading to unexpected behavior in the parsed output.

### Expected behavior

Line breaks in text content should be handled correctly during the tokenization phase. The parser should exit the "data" token before consuming the break character, ensuring that text content with line breaks is processed in the right order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
