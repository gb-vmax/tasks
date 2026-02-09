# Bug Report

### Describe the bug

After making some changes to a request, the UI doesn't reflect the updated values immediately. It seems like the application is still showing cached/stale data even though the request object has been modified.

### Reproduction

```js
// 1. Get a request by ID
const request = await getById(requestId);

// 2. Update the request with new data
await update(request, { name: 'Updated Name', url: 'https://new-url.com' });

// 3. Fetch the same request again
const updatedRequest = await getById(requestId);

// Expected: updatedRequest should have the new values
// Actual: updatedRequest still shows old values from cache
```

### Expected behavior

When a request is updated, subsequent calls to `getById()` should return the latest data, not cached values. The cache should be invalidated or refreshed when modifications are made.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues in our workflow where we need to see real-time updates to requests. It looks like something related to caching might not be working as intended.

---
Repository: /testbed
