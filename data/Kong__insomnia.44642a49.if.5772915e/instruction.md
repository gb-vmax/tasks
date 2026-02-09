# Bug Report

### Describe the bug

I'm experiencing an issue with the `unsafeRemove` function where it seems to have broken syntax. When trying to remove documents from the database, I'm getting unexpected behavior and the application is crashing.

### Reproduction

```js
const doc = {
  _id: 'req_123',
  type: 'request',
  name: 'Test Request'
};

// Try to remove the document
await database.unsafeRemove(doc);
```

The function appears to have malformed code - there's a function definition (`_archiveDocument`) that's placed inside another function in a weird way, and then there's duplicate code at the bottom that doesn't make sense. The closing brace and function signature don't match up properly.

### Expected behavior

The `unsafeRemove` function should properly remove documents from the database without syntax errors. The function should execute cleanly and remove the specified document.

### System Info
- Insomnia version: latest
- OS: macOS

This looks like it might have been introduced in a recent change to the database module. The code structure seems corrupted or incorrectly merged.

---
Repository: /testbed
