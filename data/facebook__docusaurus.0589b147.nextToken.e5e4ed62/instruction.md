# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX parser where token positions are being set incorrectly in certain contexts. When parsing MDX content, the `start` position of tokens appears to be set before the actual token reading begins, which causes position information to be off by the amount of whitespace that was skipped.

### Reproduction

```js
// Parse MDX content with leading whitespace
const content = `
  <Component />
`;

// The token positions don't align with the actual content
// start position is set before skipSpace() completes
```

This seems to happen when the parser processes tokens after skipping whitespace. The `start` position gets assigned before we know where the actual token begins.

### Expected behavior

Token positions should accurately reflect the actual start position of the token in the input, accounting for any skipped whitespace. The `start` should be set after `skipSpace()` completes so it points to the beginning of the actual token content.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
