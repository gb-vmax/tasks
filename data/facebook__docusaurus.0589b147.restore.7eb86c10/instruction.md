# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where parsing position tracking seems to be incorrect after restore operations. When the tokenizer attempts to restore state after a failed parse attempt, the position pointer appears to be set incorrectly, leading to parsing errors or unexpected behavior.

### Reproduction

```js
// When tokenizer state is restored during parsing
const tokenizer = createTokenizer(parser, initialize, from);
// ... parsing logic that triggers restore()
// The position tracking becomes corrupted
```

This happens when the tokenizer needs to backtrack during parsing - the restore function doesn't properly reset the position point, causing subsequent parsing to start from the wrong location.

### Expected behavior

After calling `restore()`, the tokenizer should properly reset to the saved `startPoint` position so that parsing can continue from the correct location. The position tracking should be accurate throughout the parsing process.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
