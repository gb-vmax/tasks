# Bug Report

### Describe the bug

The plugin API's `app.getInfo()` method is returning a syntax error when called. The application crashes when any plugin tries to access basic app information through this context method.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const info = context.app.getInfo();
    console.log(info);
  }
];
```

Running any plugin that calls `app.getInfo()` results in an error and the plugin fails to load.

### Expected behavior

The `getInfo()` method should return an object with app version and platform information without throwing errors. Plugins should be able to access this information reliably.

### System Info
- Insomnia version: latest
- OS: macOS

This seems to have broken recently, possibly after a refactor of the app context code. The method was working fine before.

---
Repository: /testbed
