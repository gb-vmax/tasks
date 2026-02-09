# Bug Report

### Describe the bug

I'm experiencing an issue with the template tag context's `util.models.request.getById` function. When I try to use it in my custom template tags, it always returns `null` even when passing valid request IDs that definitely exist in my workspace.

### Reproduction

```js
// In a custom template tag extension
async run(context) {
  const requestId = 'req_abc123'; // Valid request ID from my workspace
  const request = await context.util.models.request.getById(requestId);
  
  console.log(request); // Always prints null
  
  return request?.name || 'Request not found';
}
```

Expected the function to return the request object, but it consistently returns `null` for all request IDs I've tried.

### Steps to reproduce:
1. Create a custom template tag that uses `context.util.models.request.getById()`
2. Pass any valid request ID to the function
3. The function returns `null` instead of the request object

### Expected behavior
The function should return the request object when a valid request ID is provided, allowing template tags to access request data programmatically.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my ability to create template tags that reference other requests in the workspace. Any help would be appreciated!

---
Repository: /testbed
