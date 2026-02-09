# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the parser seems to hang or behave incorrectly when encountering certain input. The problem appears to be related to how the text tokenizer handles null/EOF characters in the input stream.

### Reproduction

```js
// When parsing markdown with specific edge cases around EOF
const processor = remark();
const result = processor.processSync('some text');

// The parser appears to enter an unexpected state
// when processing ends, potentially causing infinite loops
// or incorrect token generation
```

### Expected behavior

The parser should properly handle end-of-file conditions and gracefully terminate without entering invalid states. Token generation should complete normally and the AST should be properly formed.

### Additional context

This seems to happen specifically when the text tokenizer reaches the end of input. The state transitions don't appear to be handling the null code (EOF) correctly, which could lead to attempting to consume tokens after the data has already been entered or exited.

---
Repository: /testbed
