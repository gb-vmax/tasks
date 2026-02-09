# Bug Report

### Describe the bug

I'm experiencing an issue where template tag requests are returning stale/cached data instead of the current request state. When I update a request and then reference it using `util.models.request.getById()` in a template tag, it returns the old version of the request rather than the updated one.

### Reproduction

```js
// In a custom template tag
const request = await context.util.models.request.getById('req_123');
console.log(request.name); // Shows old name

// Meanwhile, the actual request was updated in the UI
// But the template tag still sees the cached version
```

Steps to reproduce:
1. Create a request with some initial values
2. Use a template tag that fetches the request via `getById()`
3. Update the request (change name, headers, body, etc.)
4. Execute the template tag again
5. The returned request still has the old values

This seems to happen consistently when requests are modified and then immediately accessed through template tags. The cached data persists even when the underlying request has been updated.

### Expected behavior

`getById()` should always return the current state of the request, not a cached version. If there's caching happening, it should be invalidated when the request is modified.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
