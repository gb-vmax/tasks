# Bug Report

### Describe the bug

After a recent update, the plugin API's `app.getInfo()` method is throwing a syntax error when called. The application fails to load plugins that rely on this method to retrieve version and platform information.

### Reproduction

```js
// In a plugin's main function
module.exports.requestHooks = [
  context => {
    const appInfo = context.app.getInfo();
    console.log('App version:', appInfo.version);
    console.log('Platform:', appInfo.platform);
  }
];
```

When the plugin tries to access `app.getInfo()`, the entire plugin system fails to initialize properly.

### Expected behavior

The `getInfo()` method should return an object with `version` and `platform` properties without any errors, allowing plugins to retrieve application metadata as documented in the plugin API.

### System Info
- Insomnia version: latest
- OS: macOS / Windows / Linux (affects all platforms)

This is blocking plugin development and breaking existing plugins that depend on the app context API.

---
Repository: /testbed
