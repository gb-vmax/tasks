# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in MDX where the closing fence sequence is being consumed incorrectly. When parsing code blocks, the line ending character at the end of the content appears to be consumed before exiting the `codeFlowValue` state, which causes problems with the parsing flow.

### Reproduction

```mdx
```js
console.log('test');
```
```

When this gets parsed, the line ending after the code content is being consumed in the wrong order - it's consumed before the `codeFlowValue` exit happens, which disrupts the normal tokenization flow.

### Expected behavior

The parser should exit the `codeFlowValue` state first, then handle the line ending character in the `beforeContentChunk` function. The line ending should not be consumed while still inside the `codeFlowValue` state.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
