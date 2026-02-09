# Bug Report

Title: Database find() returning stale data after document updates

I'm experiencing an issue where the `database.find()` method returns outdated results after documents have been modified. It seems like the query results are being cached somewhere and not invalidating when the underlying data changes.

### Steps to reproduce:
1. Query for a document using `database.find()`
2. Update that document using `database.update()`
3. Query again with the same parameters
4. The returned data still shows the old values instead of the updated ones

### Example:
```js
// First query
const results = await database.find('Request', { _id: 'req_123' });
console.log(results[0].name); // Outputs: "Original Name"

// Update the document
await database.update({ _id: 'req_123', name: "Updated Name" });

// Query again with same parameters
const updatedResults = await database.find('Request', { _id: 'req_123' });
console.log(updatedResults[0].name); // Still outputs: "Original Name" (should be "Updated Name")
```

This is causing issues in the UI where changes aren't reflected until the app is restarted. The problem appears consistently across different document types (Request, Response, Environment, etc.).

### Expected behavior
Each call to `database.find()` should return the current state of the documents in the database, reflecting any updates that have been made.

### Additional context
This started happening recently and is affecting workflows where documents are frequently updated. The issue persists even when using different query parameters or sort orders on the same document.

---
Repository: /testbed
