# Bug Report

### Describe the bug

The `util.models.request.getById()` method is returning `null` even when a valid request ID is provided and the request exists in the database. This is breaking template tag functionality that relies on fetching request data.

### Reproduction

```js
// In a custom template tag
const request = await context.util.models.request.getById('req_abc123');
console.log(request); // Expected: request object, Actual: null
```

Steps to reproduce:
1. Create a template tag that uses `context.util.models.request.getById()`
2. Pass a valid request ID that exists in the database
3. The method returns `null` instead of the request object

### Expected behavior

When a valid request ID is provided and the request exists in the database, `getById()` should return the request object with all its properties (id, userId, status, createdAt, updatedAt, data).

### System Info
- Insomnia version: latest
- Platform: All platforms

This seems to have started happening recently. The method is being called correctly but always returns null for existing requests.

---
Repository: /testbed
