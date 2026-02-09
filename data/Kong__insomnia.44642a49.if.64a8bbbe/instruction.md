# Bug Report

### Describe the bug

I'm experiencing an issue with `getMostRecentlyModified` function where it's returning the oldest modified document instead of the most recently modified one. The behavior seems completely inverted from what the function name suggests.

### Reproduction

```js
// Create multiple documents with different modification times
await database.insert('Request', { name: 'First', modified: 1000 });
await database.insert('Request', { name: 'Second', modified: 2000 });
await database.insert('Request', { name: 'Third', modified: 3000 });

// Try to get the most recently modified document
const mostRecent = await database.getMostRecentlyModified('Request');

// Expected: { name: 'Third', modified: 3000 }
// Actual: { name: 'First', modified: 1000 }
```

### Expected behavior

The `getMostRecentlyModified` function should return the document with the latest modification timestamp, not the oldest one.

### Additional context

This appears to be affecting any code that relies on fetching the most recently modified documents. It's causing issues in our sync logic where we need to identify the latest changes.

---
Repository: /testbed
