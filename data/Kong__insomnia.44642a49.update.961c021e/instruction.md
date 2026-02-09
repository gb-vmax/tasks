# Bug Report

### Describe the bug

After a recent update, environment variables are not maintaining their original order when modified. When I update an environment's data properties, the order gets changed unexpectedly, which is causing issues with our workflow where the order of variables matters.

### Reproduction

```js
const environment = {
  _id: 'env_123',
  data: {
    API_KEY: 'key1',
    BASE_URL: 'http://example.com',
    TOKEN: 'token123'
  },
  dataPropertyOrder: {
    API_KEY: 0,
    BASE_URL: 1,
    TOKEN: 2
  }
}

// Update the environment with new data
update(environment, {
  data: {
    API_KEY: 'key1',
    BASE_URL: 'http://example.com',
    TOKEN: 'token123'
  }
})

// The dataPropertyOrder is now being recalculated even though 
// the keys haven't changed, causing the order to be different
```

### Expected behavior

When updating an environment with the same keys in the data object, the `dataPropertyOrder` should remain unchanged. The order should only be updated when new keys are added or existing keys are removed.

### Additional context

This is particularly problematic when syncing environments across team members, as the order keeps changing on each update even when no actual changes to the variables are made.

---
Repository: /testbed
