# Bug Report

### Describe the bug

I'm experiencing an issue where request data isn't being updated properly after modifications. When I update a request and then immediately fetch it again using `getById()`, the returned data still shows the old values instead of the updated ones.

### Reproduction

```js
// Create or get a request
const request = await getById('req_123');

// Update the request
await update(request, { name: 'Updated Name' });

// Fetch the request again immediately
const updatedRequest = await getById('req_123');

// Expected: updatedRequest.name === 'Updated Name'
// Actual: updatedRequest.name still shows the old value
```

The same issue happens with `remove()` - after removing a request, calling `getById()` with the same ID still returns the deleted request data instead of null.

### Expected behavior

After updating or removing a request, subsequent calls to `getById()` should return the current state from the database, not stale cached data.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
