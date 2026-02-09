# Bug Report

### Describe the bug

After a recent update, I'm unable to retrieve proto files by their ID. The `getById()` function seems to be broken and returns `null` even when the proto file definitely exists in the database.

### Reproduction

```js
// Create a proto file
const protoFile = await protoFile.create({
  _id: 'pf_abc123',
  parentId: 'wrk_xyz',
  name: 'my-service.proto',
  // ... other fields
});

// Try to retrieve it by ID
const retrieved = await protoFile.getById('pf_abc123');
console.log(retrieved); // Returns null instead of the proto file
```

### Expected behavior

The `getById()` function should return the proto file object when called with a valid ID string. This was working fine before and is now broken.

### Additional context

This is blocking our workflow since we can't look up proto files anymore. The IDs are stored as strings in our database (like `pf_abc123`), but it seems like the lookup is failing.

---
Repository: /testbed
