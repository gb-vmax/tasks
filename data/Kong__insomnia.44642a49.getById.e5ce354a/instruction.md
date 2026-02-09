# Bug Report

### Describe the bug

I'm experiencing an issue with the `util.models.request.getById()` method in template tag contexts. When calling this method multiple times with the same request ID, it seems to return stale/cached data instead of fetching the latest version from the database.

### Reproduction

```js
// In a custom template tag
async function run(context) {
  const requestId = 'req_123';
  
  // First call - returns the request
  const request1 = await context.util.models.request.getById(requestId);
  console.log(request1.name); // "Original Name"
  
  // Update the request in the database (through UI or another process)
  // ...
  
  // Second call - should return updated request but returns cached version
  const request2 = await context.util.models.request.getById(requestId);
  console.log(request2.name); // Still shows "Original Name" instead of updated name
}
```

### Expected behavior

Each call to `getById()` should return the current state of the request from the database, not a cached version. If caching is intended, there should be cache invalidation when the underlying data changes.

### Additional context

This seems to have started happening recently. The cache appears to be storing the result but never actually checking if newer data exists in the database. This makes it impossible to get updated request data within the same template execution context.

---
Repository: /testbed
