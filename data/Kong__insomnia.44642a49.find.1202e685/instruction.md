# Bug Report

### Describe the bug

When using the `database.find()` method with a projection parameter to exclude fields, the excluded fields are still present in the returned documents. The projection doesn't seem to be applied correctly after model initialization.

### Reproduction

```js
// Try to exclude the 'created' field from results
const docs = await database.find(
  'request',
  { parentId: 'wrk_123' },
  { created: 1 },
  undefined,
  undefined,
  { created: 0 }  // Exclude 'created' field
);

// Expected: docs should not have 'created' field
// Actual: docs still contain 'created' field
console.log(docs[0].created); // This still prints the created timestamp
```

### Expected behavior

When a projection is specified to exclude certain fields (using `0` values), those fields should not appear in the returned documents. Similarly, when using inclusion projection (using `1` values), only the specified fields (plus `_id` by default) should be present in the results.

### Additional context

This seems to affect both inclusion and exclusion projections. The database query appears to execute but the projection isn't being respected in the final output.

---
Repository: /testbed
