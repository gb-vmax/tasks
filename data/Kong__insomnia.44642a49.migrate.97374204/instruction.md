# Bug Report

### Describe the bug

After a recent update, API spec objects are being returned as empty objects from the migrate function. All properties from the original spec are lost during migration, which causes the application to fail when trying to access spec properties.

### Reproduction

```js
const apiSpec = {
  _id: 'spec_123',
  type: 'ApiSpec',
  parentId: 'wrk_456',
  fileName: 'my-api.yaml',
  contents: '...',
  contentType: 'yaml'
};

const migrated = migrate(apiSpec);

// migrated is now an empty object {}
// Expected: migrated should contain all the original properties
console.log(migrated); // {}
console.log(migrated._id); // undefined
console.log(migrated.fileName); // undefined
```

### Expected behavior

The migrate function should preserve all properties from the input API spec object. The migrated object should be identical to or a valid copy of the original object with all properties intact.

### System Info

- Insomnia version: latest
- OS: macOS

This is blocking our workflow as we can't load any existing API specs anymore. The specs appear to be there in storage but come back empty after migration.

---
Repository: /testbed
