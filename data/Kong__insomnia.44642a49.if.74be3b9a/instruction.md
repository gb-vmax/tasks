# Bug Report

### Describe the bug

When comparing two models using the sync functionality, changes between objects are not being detected properly. The `describeChanges` function appears to be skipping over properties that should be compared, resulting in an empty or incomplete list of changes even when the objects have clear differences.

### Reproduction

```js
const modelA = {
  _id: 'req_123',
  name: 'Original Request',
  url: 'https://example.com',
  method: 'GET'
};

const modelB = {
  _id: 'req_123',
  name: 'Updated Request',
  url: 'https://api.example.com',
  method: 'POST'
};

const changes = describeChanges(modelA, modelB);
// Expected: array with descriptions of changed properties
// Actual: empty array or missing most changes
```

### Expected behavior

The function should return an array describing all the differences between the two model objects, excluding only keys that should be explicitly ignored (like internal metadata fields). Properties like `name`, `url`, and `method` that have different values should be included in the changes list.

### System Info
- Insomnia version: latest
- Platform: macOS

This seems to have started recently and is affecting the ability to see what's changed when syncing workspaces. Let me know if you need any additional information!

---
Repository: /testbed
