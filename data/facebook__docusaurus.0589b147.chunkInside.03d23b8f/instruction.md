# Bug Report

### Describe the bug
When parsing markdown content with certain edge cases (specifically content ending with `null`), the parser seems to hang or behave unexpectedly. The content processing doesn't complete properly and appears to get stuck in an infinite loop.

### Reproduction
```js
// Parsing markdown content that ends abruptly
const content = "Some markdown content"; // followed by null terminator

// The parser hangs when processing this content
// Expected to complete but instead becomes unresponsive
```

### Expected behavior
The parser should properly handle content that ends with a null code point and complete the tokenization process cleanly without hanging.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
