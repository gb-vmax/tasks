# Bug Report

### Describe the bug
After a recent update, I'm experiencing issues with database change buffering. When I create an indefinite buffer and try to use it, the application doesn't seem to recognize that the buffer exists or is active. This is causing problems with my database operations that rely on buffered changes.

### Reproduction
```js
// Create an indefinite buffer
const bufferId = await database.bufferChangesIndefinitely();

// Try to check if buffer is active or clear it
// The buffer ID is returned but there's no way to verify it's active
// or properly clear it when done
```

### Expected behavior
When creating an indefinite buffer, there should be a way to:
1. Check if a buffer with a given ID is currently active
2. Clear/remove a specific buffer when it's no longer needed

The buffer ID is being generated and returned, but the tracking mechanism seems to be missing or incomplete. This makes it impossible to properly manage buffer lifecycle.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
