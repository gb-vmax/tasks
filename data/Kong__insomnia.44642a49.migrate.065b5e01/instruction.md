# Bug Report

### Describe the bug

I'm experiencing an issue with proto directory objects where the prototype chain gets corrupted after migration. The object structure becomes invalid and causes unexpected behavior when trying to access properties or methods.

### Reproduction

```js
const protoDir = {
  _id: 'test-id',
  name: 'MyProto',
  // ... other properties
};

const migrated = migrate(protoDir);

// After migration, the object's prototype chain is broken
// Properties become inaccessible or behave unexpectedly
console.log(migrated.name); // May not work as expected
```

### Expected behavior

The `migrate()` function should return a valid proto directory object with the correct prototype chain intact. All properties should remain accessible after migration.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
