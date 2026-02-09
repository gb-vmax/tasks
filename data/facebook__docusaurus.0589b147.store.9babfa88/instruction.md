# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where the tokenizer's state restoration doesn't work correctly. When the parser backtracks and needs to restore a previous state, the event array doesn't get properly reset to its original length.

### Reproduction

This happens when parsing complex MDX documents that require the parser to backtrack. The tokenizer stores checkpoints using the `store()` function, but when `restore()` is called, the events array isn't being truncated to the correct position.

```js
// When the parser tries to restore a checkpoint:
// 1. Parser creates a checkpoint with store()
// 2. Parser attempts to parse some content
// 3. Parsing fails and restore() is called
// 4. The events array length is not properly restored to startEventsIndex
```

The issue is that after restoration, the events array still contains events that should have been discarded, leading to incorrect parsing results or malformed AST output.

### Expected behavior

When `restore()` is called, the `context.events` array should be truncated back to `startEventsIndex` (the length it had when `store()` was called), effectively discarding any events that were added after the checkpoint.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
