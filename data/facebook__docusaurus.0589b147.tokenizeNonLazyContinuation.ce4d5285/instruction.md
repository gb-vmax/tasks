# Bug Report

### Describe the bug

I'm encountering an issue with MDX parsing where lazy continuation lines in certain contexts are being handled incorrectly. This appears to affect how the parser processes line endings and continuation logic in specific edge cases.

The problem seems to be related to how the tokenizer determines whether to accept or reject certain line patterns. In some scenarios, lines that should be rejected are being accepted, and vice versa.

### Reproduction

```js
// MDX content that triggers the issue
const mdxContent = `
Some content with specific line continuation patterns
that should be handled differently based on lazy parsing rules
`;

// When parsing this content, the tokenizer makes incorrect decisions
// about which lines should continue and which should terminate
```

### Expected behavior

The parser should correctly distinguish between lazy and non-lazy continuation lines. Lines that are marked as lazy in the parser state should be handled according to the lazy continuation rules, while non-lazy lines should follow the standard continuation logic.

Currently, the behavior is inverted - lazy lines are being treated as non-lazy and non-lazy lines are being treated as lazy, leading to incorrect parsing results.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is affecting my ability to parse certain MDX documents correctly. Any help would be appreciated!

---
Repository: /testbed
