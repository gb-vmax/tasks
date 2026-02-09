# Bug Report

### Describe the bug

After updating to the latest version, settings migration errors are being silently swallowed. When `migrateEnsureHotKeys` throws an exception during settings migration, the error is caught but the migration continues with potentially corrupted or incomplete settings data instead of properly handling the error.

### Reproduction

```js
// Simulate a scenario where migrateEnsureHotKeys fails
const doc = {
  // settings object with invalid hotkey configuration
  hotKeyRegistry: null
};

const result = migrate(doc);
// Result contains unmigrated settings, but no error is thrown
// The application continues with broken hotkey settings
```

### Expected behavior

When settings migration fails, the error should be properly propagated or handled so that the application doesn't continue with potentially broken settings. The migration function should either:
- Successfully migrate the settings and return the migrated doc
- Throw an error if migration fails so it can be handled upstream

Currently, errors during migration are logged but then ignored, allowing the app to continue with unmigrated settings.

### System Info
- Insomnia version: latest
- OS: N/A (affects all platforms)

---
Repository: /testbed
