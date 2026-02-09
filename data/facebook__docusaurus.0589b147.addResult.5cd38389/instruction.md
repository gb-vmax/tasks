# Bug Report

### Describe the bug

I'm experiencing issues with markdown parsing where certain constructs are being resolved incorrectly. It seems like the tokenizer is not handling event resolution properly, causing some markdown elements to be processed in the wrong order or with incorrect positioning.

### Reproduction

```js
// When parsing markdown with nested constructs
const markdown = `
**bold text** with [link](url)
`;

// The events are being spliced at the wrong position
// causing the resolved output to be malformed
```

### Expected behavior

The markdown parser should correctly resolve all constructs and maintain proper event ordering. Nested elements should be processed without affecting the position of other events in the sequence.

### Additional context

This appears to affect constructs that have custom `resolve` functions. The resolved events end up in unexpected positions in the event stream, which breaks the final output.

---
Repository: /testbed
