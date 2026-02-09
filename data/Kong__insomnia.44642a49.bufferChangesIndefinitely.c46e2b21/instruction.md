# Bug Report

### Describe the bug

After a recent update, calling `bufferChangesIndefinitely()` without any arguments causes the application to break. The function now expects an options object parameter, but previously it worked fine when called with no arguments.

### Reproduction

```js
// This used to work but now fails
const bufferId = await database.bufferChangesIndefinitely();

// Error occurs because the function signature changed
// to require an options parameter
```

### Expected behavior

The function should work when called without arguments, maintaining backward compatibility. Previously, you could call `bufferChangesIndefinitely()` directly and it would return a buffer ID. Now it seems to require an options object.

### Additional context

This is breaking existing code that relies on the old function signature. The change appears to have introduced a required parameter where there wasn't one before, which breaks backward compatibility for anyone calling this function without arguments.

---
Repository: /testbed
