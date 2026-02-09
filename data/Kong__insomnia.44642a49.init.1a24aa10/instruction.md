# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC request metadata where existing saved requests are missing some properties after upgrading. When I try to access certain metadata fields on previously created gRPC requests, they return `undefined` even though new requests work fine.

### Reproduction

1. Create a gRPC request and save it
2. Restart the application or reload
3. Try to access metadata properties like `accessCount` or `createdAt`
4. These properties are undefined for requests created before the update

```js
// For existing gRPC requests
console.log(grpcRequestMeta.accessCount); // undefined
console.log(grpcRequestMeta.createdAt); // undefined

// But pinned and lastActive work fine
console.log(grpcRequestMeta.pinned); // false
console.log(grpcRequestMeta.lastActive); // 1234567890
```

### Expected behavior

All metadata properties should be available for both new and existing gRPC requests. The application should handle missing properties gracefully or migrate existing data to include the new fields.

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues when trying to sort or filter requests based on these new metadata fields.

---
Repository: /testbed
