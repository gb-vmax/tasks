# Bug Report

### Describe the bug

I'm experiencing an issue with local storage persistence in Insomnia. When a storage file doesn't exist (fresh install or after clearing data), the application fails to initialize the storage with default values. Instead of creating the file with defaults, it seems like nothing happens and subsequent reads fail or return undefined values.

### Reproduction

This happens when:
1. Starting Insomnia for the first time (no existing storage files)
2. Or after manually deleting the local storage files
3. Attempting to read a value that should fall back to defaults

The expected behavior would be that if the storage file is missing, it should be automatically created with the provided default object.

### Expected behavior

When a storage file doesn't exist, `getItem(key, defaultObj)` should:
- Create the missing file
- Initialize it with the `defaultObj` parameter
- Return the default object

Instead, it appears that the default values are not being persisted, causing issues on subsequent application launches.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
