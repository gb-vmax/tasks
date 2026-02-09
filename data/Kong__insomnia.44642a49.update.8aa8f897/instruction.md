# Bug Report

### Describe the bug

After a recent update, the environment update function is not working as expected. When I try to update an environment's data properties, the changes seem to be applied but the property order tracking (`dataPropertyOrder`) is not being maintained correctly. Additionally, I'm experiencing issues where environment name updates are being rejected even when there's no actual conflict.

### Reproduction

```js
const environment = {
  _id: 'env_123',
  parentId: 'wrk_456',
  name: 'Test Environment',
  data: {
    apiKey: 'old-key',
    baseUrl: 'https://old.api.com'
  },
  dataPropertyOrder: {
    apiKey: 0,
    baseUrl: 1
  }
};

// Try to update the environment data
await update(environment, {
  data: {
    apiKey: 'new-key',
    baseUrl: 'https://new.api.com',
    token: 'new-token'  // Adding a new property
  }
});

// Expected: dataPropertyOrder should include the new 'token' property
// Actual: The order tracking seems incorrect or missing
```

Also, when trying to rename an environment:

```js
await update(environment, {
  name: 'Updated Environment'
});

// Sometimes throws an error about name conflicts even when no conflict exists
```

### Expected behavior

1. When updating environment data with new properties, the `dataPropertyOrder` should automatically assign order values to new keys while preserving existing ones
2. When removing properties from data, their entries should be cleaned up from `dataPropertyOrder`
3. Environment name updates should only fail when there's an actual naming conflict with a sibling environment
4. The update operation should complete synchronously or return a promise consistently

### System Info
- Insomnia version: latest
- Platform: Desktop app

---
Repository: /testbed
