# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer seems to fail silently when processing certain constructs. After some investigation, it appears that the `onsuccessfulcheck` callback is not properly handling the `info` parameter, which causes the restore functionality to be skipped.

### Reproduction

```js
// When the tokenizer processes a successful check, the info.restore() 
// method should be called to restore the parser state, but this isn't happening

const parser = createParser();
const tokenizer = createTokenizer(parser, initialize, from);

// Process some MDX content with constructs that require state restoration
// The parser state is not being restored correctly after successful checks
```

### Expected behavior

When a construct check succeeds, the `info.restore()` method should be called to properly restore the parser state. The tokenizer should handle the `info` parameter correctly in the `onsuccessfulcheck` callback.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
