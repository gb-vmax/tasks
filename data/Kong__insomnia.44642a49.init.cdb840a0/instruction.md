# Bug Report

### Describe the bug

After updating to the latest version, the default settings are not being initialized correctly. The dark and light theme settings appear to be swapped, and the proxy is enabled by default when it should be disabled.

### Reproduction

```js
const settings = init();

// Expected: darkTheme should use getAppDefaultDarkTheme()
// Actual: darkTheme is using getAppDefaultLightTheme()
console.log(settings.darkTheme);

// Expected: lightTheme should use getAppDefaultLightTheme()
// Actual: lightTheme is using getAppDefaultDarkTheme()
console.log(settings.lightTheme);

// Expected: proxyEnabled should be false by default
// Actual: proxyEnabled is true
console.log(settings.proxyEnabled); // true instead of false
```

### Expected behavior

- `darkTheme` should be initialized with `getAppDefaultDarkTheme()`
- `lightTheme` should be initialized with `getAppDefaultLightTheme()`
- `proxyEnabled` should default to `false`

### System Info
- Insomnia version: latest
- OS: macOS

This is causing issues where users have the wrong theme applied on first launch and proxy settings are unexpectedly enabled.

---
Repository: /testbed
