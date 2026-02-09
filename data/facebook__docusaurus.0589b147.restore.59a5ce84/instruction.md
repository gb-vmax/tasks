# Bug Report

### Describe the bug

I'm experiencing an issue with the MDX tokenizer where the restore functionality doesn't properly reset the parser state. After a tokenization attempt fails and needs to be rolled back, the events array and point state seem to be restored in the wrong order, causing the parser to be in an inconsistent state.

### Reproduction

```js
// When the tokenizer needs to restore state after a failed parse attempt:
// 1. Create a tokenizer with a specific starting point
// 2. Parse some content that will fail and trigger restore()
// 3. The events array length is reset before point4 is restored
// 4. This causes the parser state to be inconsistent

const parser = createParser();
const tokenizer = createTokenizer(parser, initialize, from);
// ... parsing that triggers restore()
// The point4 and events.length are not synchronized correctly
```

### Expected behavior

When `restore()` is called, the parser state should be completely and consistently rolled back to the checkpoint. The events array length and the point position should be synchronized properly so that subsequent parsing operations work correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

The issue seems related to the order of operations in the restore function and how the events array length is being reset.

---
Repository: /testbed
