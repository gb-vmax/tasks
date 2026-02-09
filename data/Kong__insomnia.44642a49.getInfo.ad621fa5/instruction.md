# Bug Report

### Describe the bug

After a recent update, the plugin API's `app.getInfo()` method is returning `undefined` instead of the expected app information object. This breaks plugins that rely on getting the app version and platform information.

### Reproduction

```js
// In a plugin's context
const appInfo = app.getInfo();
console.log(appInfo); // Expected: { version: '...', platform: '...' }
                      // Actual: undefined
```

The method doesn't return anything, making it impossible for plugins to access basic app information like version and platform.

### Expected behavior

`app.getInfo()` should return an object containing at least:
- `version`: The current app version
- `platform`: The platform the app is running on

### Additional context

This appears to have broken after some recent changes to the app context module. The method was working fine in previous versions but now consistently returns undefined.

---
Repository: /testbed
