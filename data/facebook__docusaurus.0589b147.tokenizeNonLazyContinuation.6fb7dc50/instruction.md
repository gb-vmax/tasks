# Bug Report

### Describe the bug

I'm encountering an issue with lazy continuation handling in markdown parsing. It seems like the parser is incorrectly treating lazy continuations - lines that should be considered part of a lazy continuation are being rejected, while lines that shouldn't be lazy continuations are being accepted.

### Reproduction

```js
// When parsing markdown with lazy continuations like:
const markdown = `
> blockquote
lazy line
`;

// The lazy line is not being handled correctly
// Expected: lazy line should be part of the blockquote
// Actual: lazy line is treated incorrectly
```

This appears to affect block-level structures where lazy continuation is involved, particularly with blockquotes and list items.

### Expected behavior

The parser should correctly identify lazy continuation lines according to the CommonMark spec. Lines that are lazy continuations should be processed as part of the containing block, while non-lazy lines should break out of the block context.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
