# Bug Report

### Describe the bug

After a recent update, the `database.find()` function seems to have issues with field projection. When passing a projection object to exclude certain fields, those fields are still being returned in the results.

### Reproduction

```js
// Try to exclude the 'created' field from results
const results = await database.find(
  'request',
  { parentId: 'wrk_123' },
  { created: 1 },
  undefined,
  undefined,
  { created: 0 }
);

// Expected: results should not contain 'created' field
// Actual: 'created' field is still present in the returned documents
console.log(results[0].created); // Should be undefined but isn't
```

Also having issues with inclusion projections:

```js
// Try to only include specific fields
const results = await database.find(
  'request',
  {},
  { created: 1 },
  undefined,
  undefined,
  { name: 1, url: 1 }
);

// Expected: results should only contain _id, type, name, and url
// Actual: All fields are being returned
```

### Expected behavior

When using projection with exclusions (field: 0), those fields should not appear in the returned documents. When using projection with inclusions (field: 1), only the specified fields (plus _id and type) should be returned.

### Additional context

This seems to have started happening after changes to the database module. The projection parameter is being passed to NeDB correctly, but something is going wrong when the documents are being processed after retrieval.

---
Repository: /testbed
