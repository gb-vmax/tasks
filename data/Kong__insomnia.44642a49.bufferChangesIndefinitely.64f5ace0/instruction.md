# Bug Report

### Describe the bug

After a recent update, the database buffering system seems to have broken. When calling `bufferChangesIndefinitely()`, the buffer gets created but there's no way to properly track or clear it. The new helper functions `_registerIndefiniteBuffer`, `_isIndefiniteBufferActive`, and `_clearIndefiniteBuffer` were added but they're not being used anywhere in the codebase, and more importantly, there's no way to actually flush or clear these indefinite buffers once they're created.

### Reproduction

```js
// Create an indefinite buffer
const bufferId = await database.bufferChangesIndefinitely();

// Make some database changes
// ... 

// Try to flush the buffer - but there's no mechanism to do this anymore
// The buffer just sits there indefinitely with no way to clear it
```

### Expected behavior

There should be a way to flush or clear indefinite buffers after they're created. The previous implementation at least had `bufferingChanges` flag that could be toggled, but now buffers are registered in a Map with no corresponding flush mechanism exposed.

### System Info
- Insomnia version: latest
- OS: macOS

This seems like an incomplete refactoring - the helper functions were added but the actual buffer management logic wasn't fully implemented.

---
Repository: /testbed
