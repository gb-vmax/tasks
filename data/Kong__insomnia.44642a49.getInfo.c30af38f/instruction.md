# Bug Report

### Bug: app.getInfo() returns swapped version and platform values

I noticed that `app.getInfo()` is returning incorrect values - the `version` field contains the platform information and the `platform` field contains the version number. They appear to be swapped.

### Reproduction

```js
const appContext = plugins.context.app;
const info = await appContext.getInfo();

console.log(info.version);  // Expected: "2023.5.8" but got "darwin" (or "win32", "linux")
console.log(info.platform); // Expected: "darwin" but got "2023.5.8"
```

### Expected behavior

- `info.version` should return the application version (e.g., "2023.5.8")
- `info.platform` should return the platform name (e.g., "darwin", "win32", "linux")

Currently these values are reversed.

### Additional context

This is breaking plugins that rely on checking the app version for compatibility or the platform for platform-specific behavior.

---
Repository: /testbed
