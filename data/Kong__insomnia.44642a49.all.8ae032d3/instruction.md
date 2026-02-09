# Bug Report

### Describe the bug

When calling the `all()` function to retrieve workspace metadata, the last item in the results is being incorrectly removed. This causes the most recently created or last workspace meta entry to be missing from the returned array.

### Reproduction

```js
// Create multiple workspace meta entries
await createWorkspaceMeta('workspace-1');
await createWorkspaceMeta('workspace-2');
await createWorkspaceMeta('workspace-3');

// Retrieve all workspace meta
const allMeta = all();

// Expected: 3 items
// Actual: 2 items (last one is missing)
console.log(allMeta.length); // Returns 2 instead of 3
```

### Expected behavior

The `all()` function should return all workspace metadata entries from the database without removing any items. All valid workspace meta objects with an `id` should be included in the results.

### Additional context

This seems to have started happening recently. The function is filtering out items without an `id` (which makes sense) but then also removing the last valid item from the array, which doesn't seem intentional.

---
Repository: /testbed
