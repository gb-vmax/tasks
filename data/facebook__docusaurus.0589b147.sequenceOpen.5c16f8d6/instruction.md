# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with non-`#` characters at the beginning are being incorrectly processed. It seems like the parser is consuming characters it shouldn't be consuming, leading to malformed heading output.

### Reproduction

```js
// This should not be parsed as a valid heading
const input = `! This should not be a heading`;

// Parser incorrectly processes this
// Expected: Not recognized as heading
// Actual: Processed as if it were a heading sequence
```

When I try to parse markdown with characters that have ASCII codes less than or equal to 35 (the `#` character), they're being treated as part of the heading sequence when they shouldn't be.

### Expected behavior

Only the `#` character (ASCII 35) should be consumed as part of the ATX heading sequence. Other characters with lower ASCII values (like `!`, space, etc.) should cause the parser to reject the sequence as an invalid heading.

The parser should strictly validate that only `#` characters are present in the heading marker sequence.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
