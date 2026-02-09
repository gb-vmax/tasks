# Bug Report

### Describe the bug

I'm experiencing an issue where updating existing documents in the database doesn't work as expected. When I try to update a document, it seems like the operation is not being performed correctly and the changes aren't being persisted.

### Reproduction

```js
// Create a document first
const doc = await database.insert({
  type: 'Request',
  name: 'My Request',
  url: 'https://example.com'
});

// Try to update the document
const updatedDoc = await database.update({
  ...doc,
  name: 'Updated Request',
  url: 'https://newurl.com'
});

// The update doesn't seem to work properly
console.log(updatedDoc); // Expected updated values, but behavior is incorrect
```

### Expected behavior

The `database.update()` method should properly update existing documents and persist the changes. The updated document should reflect the new values.

### Additional context

This seems to have started happening recently. The database operations were working fine before, but now updates are behaving strangely. I'm not sure if this is related to the sync functionality or something else in the database layer.

---
Repository: /testbed
