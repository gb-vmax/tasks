# Bug Report

### Describe the bug

I'm experiencing an issue with text slicing in markdown parsing where the last character of tokens is being incorrectly included or excluded. This appears to be happening when extracting chunks of text from the parser buffer.

### Reproduction

When parsing markdown content, tokens that should end at a specific position are including an extra character at the end. For example:

```js
// Input markdown with a token spanning from position 0 to position 5
// Expected: "hello"
// Actual: "hello " (includes extra character)
```

This seems to affect cases where:
1. The start and end indices are the same (single chunk)
2. The end buffer index is at position 0

### Expected behavior

The sliced chunks should contain exactly the characters within the token boundaries, without including extra characters at the end or missing characters when the end position is at index 0.

### Additional context

This is causing issues with markdown parsing where tokens are not being extracted with the correct boundaries. The problem appears to be related to how the buffer indices are being used when slicing chunks.

---
Repository: /testbed
