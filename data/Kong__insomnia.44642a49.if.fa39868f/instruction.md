# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request operations where updates to requests don't seem to be reflected immediately. When I modify a request and then immediately try to fetch it again, I'm getting stale data instead of the updated values.

### Reproduction

```js
// Update a request
await update(myRequest, { name: 'Updated Name' });

// Immediately fetch it back
const fetched = await getById(myRequest._id);

// Expected: fetched.name === 'Updated Name'
// Actual: fetched.name still has the old value
```

The same issue happens with `remove()` - if I delete a request and then try to fetch it, it still returns the deleted request instead of null.

### Expected behavior

When a request is updated or removed, subsequent calls to `getById()` should return the current state from the database, not cached/stale data.

### Additional context

This seems to have started happening recently. I noticed it when working with WebSocket requests specifically, but it might affect other request types too. The data does eventually update if I wait a few seconds and retry, but that's not ideal for my use case where I need immediate consistency.

---
Repository: /testbed
