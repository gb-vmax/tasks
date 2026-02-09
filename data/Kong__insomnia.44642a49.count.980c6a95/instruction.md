# Bug Report

### Describe the bug

I'm experiencing an issue with the database count function after a recent update. When I call `database.count()` on a collection after making changes to documents, the count result seems to be stale and doesn't reflect the actual current state of the database.

### Reproduction

```js
// Initial count
const initialCount = await database.count('requests', { workspaceId: 'abc123' });
console.log(initialCount); // e.g., 5

// Add a new document
await database.insert({ type: 'requests', workspaceId: 'abc123', name: 'New Request' });

// Count again immediately
const newCount = await database.count('requests', { workspaceId: 'abc123' });
console.log(newCount); // Still shows 5, expected 6
```

The count doesn't update even though a new document was inserted. If I wait a few seconds and call count again, it returns the correct value.

### Expected behavior

The count should immediately reflect any changes made to the database. When documents are inserted, updated, or deleted, subsequent count queries should return the updated count without any delay.

### Additional context

This seems to have started happening recently. The count eventually becomes correct after some time passes, but this is causing issues in our UI where we display document counts that are temporarily incorrect.

---
Repository: /testbed
