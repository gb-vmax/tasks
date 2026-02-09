# Bug Report

### Describe the bug

I'm experiencing an issue where markdown parsing fails when processing documents that end without a newline. The parser seems to be consuming the null terminator incorrectly and then trying to process additional data, which causes unexpected behavior.

### Reproduction

```js
const processor = remark();

// This causes issues when the document ends abruptly
const result = processor.processSync('# Hello World');

// The parser tries to enter "data" mode even after consuming null
// Leading to incorrect AST generation
```

### Expected behavior

The parser should properly handle the end of input (null code) and stop processing without attempting to enter additional states or consume more characters after the null terminator.

### Additional context

This appears to happen specifically when the document doesn't have a trailing newline. The parser consumes the null code but then continues execution instead of returning early, which leads to incorrect token generation.

---
Repository: /testbed
