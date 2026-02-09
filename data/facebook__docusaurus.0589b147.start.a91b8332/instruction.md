# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where whitespace handling appears broken. The parser seems to be entering a space token state even when no space character is present, which causes unexpected behavior in the output.

### Reproduction

```js
// Parse markdown with specific spacing patterns
const result = remark().parse('text');

// The parser incorrectly handles the space state
// Expected: normal parsing without space token for non-space characters
// Actual: space token is entered regardless of character type
```

When processing markdown text, the space tokenizer is being triggered even for non-space characters. This leads to incorrect AST generation and malformed output.

### Expected behavior

The space tokenizer should only enter the space token state when it actually encounters a space character (as determined by `markdownSpace(code2)`). Non-space characters should skip the space token entirely and proceed directly to the next state.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like a regression in the space handling logic. The tokenizer is unconditionally entering a state it shouldn't be in for certain characters.

---
Repository: /testbed
