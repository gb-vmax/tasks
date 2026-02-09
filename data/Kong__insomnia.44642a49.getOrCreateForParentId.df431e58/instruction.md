# Bug Report

### Describe the bug

I'm experiencing an issue with cookie jar creation where multiple cookie jars are being created for the same parent ID. When I check my workspace, I'm seeing duplicate cookie jars instead of reusing the existing one.

### Reproduction

```js
// Get or create cookie jar for a workspace
const cookieJar1 = await getOrCreateForParentId('workspace_123');

// Later, try to get the same cookie jar
const cookieJar2 = await getOrCreateForParentId('workspace_123');

// Expected: cookieJar1 and cookieJar2 should be the same
// Actual: A new cookie jar gets created even though one already exists
```

### Expected behavior

When calling `getOrCreateForParentId()` with the same parent ID, it should return the existing cookie jar if one already exists. Only when no cookie jar exists should a new one be created.

Currently it seems like the function is creating new cookie jars even when one is already present, leading to duplicates in the database.

### System Info
- Insomnia version: Latest
- OS: macOS

---
Repository: /testbed
