# Bug Report

### Describe the bug

I'm experiencing an issue with the markdown parser where it's consuming code twice when processing certain text content. This appears to happen when the parser encounters a null code point - it seems to be calling `effects.consume(code2)` twice in the `notText` function, which leads to incorrect parsing behavior.

### Reproduction

```js
// When parsing markdown with specific null terminators
const input = "Some text content";
const result = remark().parse(input);

// The parser incorrectly processes the end of the content
// Effects are consumed twice leading to unexpected token boundaries
```

### Expected behavior

The parser should only consume each code point once. When a null code point is encountered, it should be consumed and then return, not consumed again after the conditional check.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like it could cause issues with any markdown content that has specific boundary conditions. The double consumption is causing the parser to skip ahead unexpectedly.

---
Repository: /testbed
