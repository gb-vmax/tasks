# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with document retrieval in the database layer. When fetching documents that have parent-child relationships, the system seems to be returning stale or incorrect data. Specifically, when I update a document and then immediately fetch it again, I sometimes get the old version instead of the updated one.

### Reproduction

```js
// Create a document with a parent
const parent = await database.insert({ type: 'workspace', name: 'My Workspace' });
const child = await database.insert({ type: 'request', name: 'My Request', parentId: parent._id });

// Update the child document
await database.update({ ...child, name: 'Updated Request' });

// Fetch the document again
const fetched = await database.get('request', child._id);

// Expected: fetched.name === 'Updated Request'
// Actual: fetched.name === 'My Request' (sometimes returns old value)
```

### Additional context

This seems to happen more frequently when:
1. Documents are updated in rapid succession
2. The documents have parent-child relationships
3. Multiple documents are being fetched/updated concurrently

The issue is intermittent but reproducible with the above pattern. Sometimes it returns the correct updated value, other times it returns the stale data.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
