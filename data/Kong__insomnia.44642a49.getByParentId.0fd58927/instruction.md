# Bug Report

### Describe the bug

I'm experiencing an issue where gRPC request metadata is not being retrieved correctly. When trying to fetch metadata by parent ID, it seems like the wrong data is being returned or no data is found at all.

### Reproduction

```js
// Try to get gRPC request metadata for a specific request
const parentId = 'req_abc123';
const metadata = getByParentId(parentId);

// Expected: metadata for the request with ID 'req_abc123'
// Actual: null or incorrect metadata
```

### Expected behavior

The `getByParentId()` function should return the gRPC request metadata associated with the given parent request ID. Instead, it appears to be using the wrong value for the query, resulting in either no results or incorrect results being returned.

### Additional context

This seems to have started happening recently. The metadata exists in the database but just isn't being retrieved properly when queried by parent ID. Other similar functions in the codebase seem to work fine, so this might be specific to the gRPC request metadata retrieval.

---
Repository: /testbed
