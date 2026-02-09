# Bug Report

### Describe the bug

I'm encountering an issue where gRPC request metadata is not being retrieved correctly. When trying to access existing request metadata, it seems like the system is attempting to create new metadata with invalid parameters instead of returning the existing one.

### Reproduction

```js
// Try to get or create gRPC request metadata
const parentId = 'some-valid-parent-id';
const meta = await getOrCreateByParentId(parentId);

// Expected: Should return existing metadata or create new one with parentId
// Actual: Fails or creates metadata with wrong parentId value
```

### Steps to reproduce:
1. Create a gRPC request with metadata
2. Call `getOrCreateByParentId()` with the parent request ID
3. The function fails to return the existing metadata properly

### Expected behavior

When metadata exists for a given parentId, it should be returned. When it doesn't exist, new metadata should be created with the correct parentId string value.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently as it was working fine before. The metadata retrieval logic appears to have regressed.

---
Repository: /testbed
