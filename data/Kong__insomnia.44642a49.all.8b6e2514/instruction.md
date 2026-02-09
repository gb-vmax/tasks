# Bug Report

### Duplicate function declarations causing issues with API spec operations

I'm encountering a problem where operations on API specs aren't behaving as expected. It seems like updates aren't being reflected properly and the data returned isn't consistent.

### Reproduction
```js
// Create or update an API spec
await updateOrCreateForParentId(workspaceId, { name: 'Updated Spec' });

// Fetch all specs
const specs = await all();

// The updated spec doesn't appear with the correct data
// or operations fail silently
```

### Expected behavior
When updating or creating API specs, the changes should be reflected immediately in subsequent queries. The `all()` function should return the current state of all specs without any conflicts.

### Additional context
This started happening recently and seems to affect multiple API spec operations. Sometimes the functions don't work at all, and other times they return stale or incorrect data.

---
Repository: /testbed
