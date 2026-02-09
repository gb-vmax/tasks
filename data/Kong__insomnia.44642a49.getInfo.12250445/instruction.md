# Bug Report

### Describe the bug

The `app.getInfo()` method is returning incorrect data after a recent update. The method appears to have issues with its structure and is not returning the expected object format.

### Reproduction

```js
const appContext = plugins.createAppContext();
const info = appContext.app.getInfo();

console.log(info);
// Expected: { version: '...', platform: '...' }
// Actual: Returns malformed object or throws error
```

### Steps to reproduce
1. Call `app.getInfo()` from a plugin context
2. Try to access the returned object properties
3. Notice that the object structure is broken or contains unexpected properties

### Expected behavior

The method should return a simple object with `version` and `platform` properties as it did before. The object should be properly structured and immediately accessible without any initialization issues.

### Additional context

This seems to have broken after some recent changes to the app context. The method was working fine in previous versions and plugins relying on this are now failing.

---
Repository: /testbed
