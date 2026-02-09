# Bug Report

### Describe the bug

After migrating an API spec, the original document object gets mutated and loses its `_id` property. This is causing issues when trying to reference or work with the original spec object after migration.

### Reproduction

```js
const apiSpec = {
  _id: 'spec_123',
  name: 'My API',
  contents: '...'
};

const migrated = migrate(apiSpec);

// Original object is now missing _id
console.log(apiSpec._id); // undefined (expected: 'spec_123')
```

### Expected behavior

The `migrate()` function should not mutate the original document. The input object should remain unchanged after migration, and only the returned object should reflect any transformations.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
