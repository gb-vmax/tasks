# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC request metadata retrieval. When trying to fetch metadata by parent ID, the function appears to be returning the wrong data. Instead of getting the metadata associated with a specific parent request, it seems like the query is using the wrong field.

### Reproduction

```js
// Create a gRPC request with ID 'req_123'
const grpcRequest = { id: 'req_123', ... }

// Create metadata with parentId pointing to the request
const metadata = { 
  id: 'meta_456',
  parentId: 'req_123',
  ...
}

// Try to get metadata by parent ID
const result = getByParentId('req_123')

// Expected: metadata with parentId === 'req_123'
// Actual: returns nothing or wrong data
```

### Expected behavior

`getByParentId(parentId)` should return the metadata where `parentId` matches the provided ID, not where the metadata's own `id` matches.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our ability to properly load gRPC request metadata in the UI. Any help would be appreciated!

---
Repository: /testbed
