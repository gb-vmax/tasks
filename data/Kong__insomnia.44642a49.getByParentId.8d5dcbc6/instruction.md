# Bug Report

### Describe the bug

The `getByParentId` function in the gRPC request meta model is returning the wrong value. Instead of returning the actual request metadata results, it's returning the `parentId` string that was passed in as a parameter.

### Reproduction

```js
const parentId = 'req_123abc';
const meta = getByParentId(parentId);

// Expected: meta should be the GrpcRequestMeta object
// Actual: meta is just the string 'req_123abc'
```

When trying to retrieve gRPC request metadata by parent ID, the function just returns the ID itself instead of the actual metadata object from the database. This makes it impossible to access any of the metadata properties.

### Expected behavior

The function should return the `GrpcRequestMeta` object(s) that match the given `parentId`, not the `parentId` string itself.

### System Info
- Insomnia version: latest
- OS: any

---
Repository: /testbed
