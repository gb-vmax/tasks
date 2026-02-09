# Bug Report

### Describe the bug

I'm encountering an issue with the tokenizer's `write` function where it's returning the wrong value when processing chunks. Instead of returning an empty array when chunks are still being processed, it's returning the chunks array itself, which causes downstream parsing issues.

### Reproduction

```js
const tokenizer = createTokenizer(parser, initialize, from);

// Write some content that needs to be tokenized
const result = tokenizer.write(someSlice);

// Expected: result should be [] when processing is incomplete
// Actual: result is the chunks array when the first chunk is not null
```

When the tokenizer is still processing and hasn't completed, the `write` function should return an empty array to indicate that no events are ready yet. However, it's currently checking the wrong condition and returning the chunks array instead.

### Expected behavior

The `write` function should:
1. Return an empty array `[]` when chunks are still being processed (i.e., when the last chunk is not null)
2. Only return the resolved events array when processing is complete

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems to be causing issues with markdown parsing where partial content is being incorrectly processed as complete.

---
Repository: /testbed
