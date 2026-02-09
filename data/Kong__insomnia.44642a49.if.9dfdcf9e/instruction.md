# Bug Report

### Describe the bug

When duplicating a request, the duplicate operation seems to be broken. The code appears to have duplicate function definitions and unreachable code paths, which causes the duplication functionality to not work as expected.

### Reproduction

```js
// Try to duplicate any request (gRPC, WebSocket, or regular HTTP request)
const originalRequest = {
  _id: 'req_123',
  name: 'My Request',
  parentId: 'folder_456',
  isPrivate: false,
  // ... other fields
};

// Attempt to duplicate with custom patch
const duplicated = await duplicate(originalRequest, { name: 'Custom Name' });
```

### Expected behavior

The request should be duplicated successfully with:
- Sanitized fields (`_id`, `created`, `modified`, `parentId` removed from patch)
- Proper name handling (e.g., "My Request (copy)" or incrementing copy numbers)
- The `isPrivate` flag preserved if not overridden

### Actual behavior

The duplication process likely fails or behaves unexpectedly due to syntax errors in the code structure. There appear to be helper functions defined inside the duplicate function and unreachable code after the return statements.

### System Info
- Insomnia version: Latest
- The issue is in `packages/insomnia/src/models/helpers/request-operations.ts`

This looks like it might have been introduced during a refactoring where the helper functions were being extracted but the old code wasn't properly removed.

---
Repository: /testbed
