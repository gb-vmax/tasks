# Bug Report

### Describe the bug

I'm experiencing an issue with attention sequences (emphasis/strong markers like `*` and `_`) not being parsed correctly. It seems like the tokenizer is trying to use the result of `inside()` before properly setting up the attention sequence context.

### Reproduction

```js
const markdown = '*emphasis text*'
// or
const markdown = '**strong text**'

// When parsing, the attention markers are not being recognized properly
// The sequence entry happens after inside() is called instead of before
```

### Expected behavior

Attention sequences should be properly tokenized with the sequence entry happening before the inside function is called. The markers should be consumed in the correct order within the established attention sequence context.

### System Info
- remark version: 15.0.1
- Node version: Latest

This appears to have broken after a recent change to the tokenization flow. The order of operations seems incorrect now.

---
Repository: /testbed
