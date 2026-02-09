# Bug Report

### Describe the bug

I'm encountering an issue where proto files cannot be retrieved by their ID. When trying to fetch a proto file using `getById()`, it returns `null` even though the proto file exists in the database.

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

// retrieved is null instead of the proto file object
console.log(retrieved); // null
```

### Expected behavior

`getById()` should return the proto file object when a valid ID is provided. The function worked correctly before but now always returns `null`.

### Additional context

This seems to affect all proto file lookups by ID. Other model methods like `getByParentId()` still work fine, so it's specific to the ID-based lookup.

---
Repository: /testbed
