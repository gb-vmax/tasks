# Bug Report

### Describe the bug

The `getOrCreateForParentId` function is not creating a base environment when none exists. Instead, it's trying to create one when environments already exist, which causes the function to return undefined when called on a parent that has no environments yet.

### Reproduction

```js
// Call getOrCreateForParentId with a parentId that has no environments
const parentId = 'wrk_new123';
const env = await getOrCreateForParentId(parentId);

// Expected: A new base environment to be created and returned
// Actual: undefined is returned because no environment exists
console.log(env); // undefined
```

### Expected behavior

When calling `getOrCreateForParentId` with a parentId that doesn't have any environments yet, the function should:
1. Detect that no environments exist
2. Create a new base environment with a deterministic ID
3. Return the newly created environment

Currently it seems like the logic is inverted - it only attempts to create an environment when one already exists, and returns undefined when the environments array is empty.

### System Info
- Insomnia version: Latest
- OS: Any

---
Repository: /testbed
