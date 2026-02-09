# Bug Report

### Describe the bug

When updating environment data with new properties, the `dataPropertyOrder` field is not being automatically updated to include the new keys. This causes issues with the ordering system when new environment variables are added.

### Reproduction

```js
const environment = {
  _id: 'env_1',
  data: {
    existingVar: 'value1'
  },
  dataPropertyOrder: {
    existingVar: 0
  }
};

// Update with new property
update(environment, {
  data: {
    existingVar: 'value1',
    newVar: 'value2'
  }
});

// Expected: dataPropertyOrder should include 'newVar' with appropriate sort key
// Actual: dataPropertyOrder remains unchanged, only contains 'existingVar'
```

### Expected behavior

When new properties are added to the `data` object during an update, the `dataPropertyOrder` should automatically be updated to include those new keys with appropriate sort values. The sort values should be incremented from the maximum existing sort key to maintain proper ordering.

### Additional context

This affects the UI display order of environment variables. Without the proper `dataPropertyOrder` entries, new variables may not appear in the expected position or could cause rendering issues.

---
Repository: /testbed
