# Bug Report

### Describe the bug
When creating a new gRPC request, the `parentId` validation check happens after the document is already created in the database. This means that even if a `parentId` is not provided, the request gets created with `undefined` as the parent, and then an error is thrown afterwards.

### Reproduction
```js
// Try to create a gRPC request without parentId
const grpcRequest = create({
  name: 'My Request',
  // parentId is missing
});
```

### Expected behavior
The validation should happen before creating the document in the database. If `parentId` is missing, an error should be thrown and no document should be created.

Currently, a document with `parentId: undefined` gets created in the database before the error is thrown, which leaves orphaned/invalid data.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
