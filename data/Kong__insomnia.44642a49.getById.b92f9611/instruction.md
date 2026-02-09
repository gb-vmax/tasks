# Bug Report

### Describe the bug

The `util.models.request.getById()` method in template tag contexts is always returning `null` regardless of the request ID provided. This breaks any template tags or plugins that rely on fetching request data by ID.

### Reproduction

```js
// In a custom template tag
async run(context) {
  const requestId = 'req_123abc';
  const request = await context.util.models.request.getById(requestId);
  
  console.log(request); // Always prints null, even for valid IDs
  
  // Expected: Should return the request object
  // Actual: Always returns null
}
```

### Expected behavior

When calling `getById()` with a valid request ID, it should return the corresponding request object. It should only return `null` if the request doesn't exist.

### Additional context

This seems to have started happening recently. Previously, this method would correctly fetch and return request objects. Now it consistently returns `null` for all request IDs, breaking functionality that depends on cross-referencing requests in templates.

---
Repository: /testbed
