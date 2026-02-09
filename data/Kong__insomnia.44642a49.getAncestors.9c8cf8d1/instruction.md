# Bug Report

### Describe the bug

I'm experiencing an issue with template tag functions that use `request.getAncestors()`. After a recent update, the ancestors are being returned in an unexpected order. Previously, they came back in the natural database order, but now they seem to be sorted/reordered somehow.

This is causing problems in my custom templates where I was relying on the original ordering of ancestors to traverse the request hierarchy correctly.

### Reproduction

```js
// In a custom template tag
const ancestors = await context.models.request.getAncestors(currentRequest);

// ancestors now comes back in a different order than before
// Expected: natural DB order (as returned by db.withAncestors)
// Actual: reordered by type (request groups first, then workspaces)
```

### Steps to reproduce:
1. Create a request nested under multiple request groups
2. Use a template tag that calls `request.getAncestors()`
3. Observe the order of returned ancestors

### Expected behavior

The ancestors should be returned in their natural hierarchy order as stored in the database, not reordered by type. This was the behavior in previous versions and changing it breaks existing template logic that depends on the original ordering.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
