# Bug Report

### Describe the bug

After creating new settings, the returned settings object doesn't contain the expected default values. It appears that the newly created settings are being retrieved incorrectly, returning `null` or an incomplete object instead of the freshly created settings with all default properties.

### Reproduction

```js
// Create new settings
const newSettings = await create();

// Expected: newSettings should contain all default values from the creation
// Actual: newSettings is null or missing properties
console.log(newSettings); // null or incomplete object
```

### Expected behavior

When creating new settings via the `create()` function, it should return the complete settings object with all default values that were just created. The returned object should match what was created by `db.docCreate<Settings>(type)`.

### System Info
- Insomnia version: latest
- OS: N/A

---
Repository: /testbed
