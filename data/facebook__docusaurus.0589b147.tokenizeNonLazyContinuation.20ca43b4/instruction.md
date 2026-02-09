# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where line continuation logic appears to be inverted. When parsing multi-line content, the parser is treating lazy continuation lines incorrectly - it's accepting lines that should be rejected and rejecting lines that should be accepted.

### Reproduction

```js
const markdown = `
> Quote line 1
  Continuation line
> Quote line 2
`;

const result = remark().parse(markdown);
// The continuation line is being processed incorrectly
```

This seems to affect blockquotes and other block-level elements that support lazy continuation. The parser is making the wrong decision about whether a line should continue the previous block or start a new one.

### Expected behavior

Lines that are valid continuations should be properly attached to their parent blocks, and lines that aren't valid continuations should be handled as separate blocks or content.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
