# Bug Report

### Describe the bug
When trying to retrieve a proto file by ID using `getById()`, the function returns `null` even though the proto file exists in the database. This breaks functionality that depends on looking up proto files by their ID.

### Reproduction
```js
// Create a proto file
const protoFile = await models.protoFile.create({
  parentId: 'wrk_123',
  name: 'test.proto',
  protoText: 'syntax = "proto3";'
});

// Try to retrieve it by ID
const retrieved = await models.protoFile.getById(protoFile._id);

// retrieved is null, but should be the proto file object
console.log(retrieved); // null
console.log(protoFile._id); // 'pf_abc123...'
```

### Expected behavior
The `getById()` function should return the proto file object when a valid ID is passed. Other model methods that retrieve by ID work correctly, so this seems specific to proto files.

### Additional context
This appears to have broken recently - proto file lookups were working fine before. The issue affects any workflow that needs to fetch proto files by their ID, including the gRPC request functionality.

---
Repository: /testbed
