# Bug Report

### Describe the bug

After a recent update, I'm experiencing issues with request retrieval in Insomnia. When fetching requests by ID, the function seems to be returning stale or incorrect data in some cases. The behavior is inconsistent - sometimes it works fine, other times it returns outdated request objects.

### Reproduction

```js
// Fetch a request multiple times
const request1 = await getById('req_123abc');
console.log(request1.name); // "Original Name"

// Update the request in the database
await updateRequest('req_123abc', { name: 'Updated Name' });

// Fetch again - sometimes returns old data
const request2 = await getById('req_123abc');
console.log(request2.name); // Expected: "Updated Name", Got: "Original Name"
```

It seems like there's some caching happening that's not being invalidated properly when the underlying data changes. This is particularly problematic when:
1. Updating a request
2. Immediately fetching it again
3. The old cached version is returned instead of the updated one

### Expected behavior

`getById()` should always return the most current version of a request from the database, not a cached copy that may be out of date.

### System Info
- Insomnia version: Latest
- OS: macOS

This is causing issues in workflows where requests are updated frequently and need to be re-fetched to get the latest state.

---
Repository: /testbed
