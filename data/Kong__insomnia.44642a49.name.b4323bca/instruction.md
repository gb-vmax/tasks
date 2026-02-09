# Bug Report

### Describe the bug

I'm experiencing an issue with merge conflict name generation. It seems like the name field is now generating sequential numbered names instead of returning a simple static name. This is causing problems when I need to reference merge conflicts by name, as the names keep incrementing unexpectedly.

### Reproduction

```js
// Creating multiple merge conflicts
const conflict1 = mergeConflictSchema.name();
const conflict2 = mergeConflictSchema.name();

// Expected both to be 'name'
// But getting 'name-1', 'name-2', etc.
```

The name generator appears to be using some kind of counter that persists across calls, which wasn't the case before. Each time I call the name function, it returns a different value with an incrementing number suffix.

### Expected behavior

The `name` field should return a consistent value (just `'name'`) every time it's called, similar to how other fields like `message` work. If I need unique names, I should be able to control that myself rather than having it automatically increment.

### Additional context

This seems to have changed recently. The previous behavior was to just return a static string. Now there's some state being maintained that causes the names to increment, which breaks my code that expects consistent naming.

---
Repository: /testbed
