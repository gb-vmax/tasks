# Bug Report

### Describe the bug
The `util.models.request.getById()` method is always returning `null` for all request IDs. It seems like the method is no longer fetching requests from the actual data source.

### Reproduction
```js
const context = {
  util: {
    models: {
      request: {
        getById: async (id) => {
          // Always returns null regardless of the ID
          const result = await context.util.models.request.getById('req_123');
          console.log(result); // null
          return result;
        }
      }
    }
  }
};
```

Steps to reproduce:
1. Call `util.models.request.getById()` with a valid request ID
2. The method returns `null` instead of the request object
3. This happens for all request IDs, even ones that definitely exist

### Expected behavior
The method should return the request object when called with a valid request ID that exists in the workspace.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have started happening recently. Previously this method would correctly fetch and return request objects.

---
Repository: /testbed
