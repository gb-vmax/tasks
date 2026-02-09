# Bug Report

### Describe the bug
After a recent update, the settings initialization is failing silently. When the app starts up for the first time or when settings need to be created, it seems like the settings object is not being properly initialized, causing the application to behave as if no settings exist.

### Reproduction
```js
// Try to initialize settings on first run
const settings = await create();

// settings is now undefined instead of the created settings object
console.log(settings); // undefined
```

This appears to happen when:
1. Starting the application for the first time
2. When settings need to be recreated for any reason
3. The created settings document exists but cannot be retrieved immediately

### Expected behavior
The `create()` function should return the newly created settings object, not `undefined`. The application should be able to access default settings after initialization.

### System Info
- Insomnia version: latest
- OS: Various

---
Repository: /testbed
