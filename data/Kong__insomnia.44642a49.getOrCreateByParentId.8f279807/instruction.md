# Bug Report

### Describe the bug

I'm experiencing an issue with gRPC request metadata where `getOrCreateByParentId` is not returning the correct object. When calling this function, it seems to be returning the wrong metadata instance regardless of whether one already exists or not.

### Reproduction

```js
// First call - should create new metadata
const meta1 = await getOrCreateByParentId('request-123');

// Second call - should return existing metadata
const meta2 = await getOrCreateByParentId('request-123');

// Expected: meta1 and meta2 should be the same object
// Actual: They appear to be different instances or one is undefined
```

### Expected behavior

- If metadata doesn't exist for a parentId, create and return a new one
- If metadata already exists for a parentId, return the existing one
- Multiple calls with the same parentId should return the same metadata object

### Additional context

This is causing issues when working with gRPC requests as the metadata is not being properly reused. It looks like the function logic might be inverted somehow - I'm getting unexpected results when trying to retrieve existing metadata.

---
Repository: /testbed
