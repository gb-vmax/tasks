# Bug Report

### Describe the bug

I'm experiencing an issue where database count queries are returning stale results after documents are modified. When I update or create documents, subsequent count queries still return the old count value instead of reflecting the actual current state of the database.

### Reproduction

```js
// Initial count
const initialCount = await database.count('Request', { parentId: 'workspace_1' });
console.log(initialCount); // e.g., 5

// Create a new document
await database.docCreate('Request', {
  parentId: 'workspace_1',
  name: 'New Request'
});

// Count again immediately
const newCount = await database.count('Request', { parentId: 'workspace_1' });
console.log(newCount); // Still shows 5 instead of 6!
```

The same issue happens with updates and deletes - the count doesn't reflect changes made to the database.

### Expected behavior

The count should always return the current number of documents matching the query, reflecting any recent changes to the database.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. The counts eventually update after waiting a few seconds, but they should be accurate immediately after making changes.

---
Repository: /testbed
