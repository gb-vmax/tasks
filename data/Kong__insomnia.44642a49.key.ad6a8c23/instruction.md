# Bug Report

### Describe the bug
I'm experiencing a syntax error in the snapshot state entry schema that's preventing the application from running. It looks like there's an issue with the schema definition in `type-schemas.ts`.

### Reproduction
When trying to use the sync functionality, the application fails to start with a syntax error. The error appears to be related to the `snapshotStateEntrySchema` object definition.

Looking at the code structure:
```js
export const snapshotStateEntrySchema: Schema<SnapshotStateEntry> = {
  blob: () => 'blob',
  // ... some key generation logic here
  name: () => 'name',
};
```

The schema object seems to have malformed syntax that prevents proper parsing.

### Expected behavior
The `snapshotStateEntrySchema` should be a valid JavaScript object that can be properly parsed and used by the sync system.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking my ability to use the sync features. Any help would be appreciated!

---
Repository: /testbed
