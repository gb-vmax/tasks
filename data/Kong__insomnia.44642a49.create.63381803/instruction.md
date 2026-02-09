# Bug Report

### Describe the bug

When creating a new GrpcRequestMeta object, the `parentId` field is being removed from the created document even though it's a required field. This causes the created object to be missing its parent reference.

### Reproduction

```js
const meta = await models.grpcRequestMeta.create({
  parentId: 'req_123',
  // other fields...
});

// meta.parentId is undefined, but it should be 'req_123'
console.log(meta.parentId); // undefined
```

### Expected behavior

The created GrpcRequestMeta object should retain the `parentId` field that was passed in during creation. The parent validation should happen without removing the field from the final object.

### System Info
- Insomnia version: latest
- Platform: All platforms

---
Repository: /testbed
