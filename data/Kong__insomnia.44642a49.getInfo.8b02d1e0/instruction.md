# Bug Report

### Describe the bug

The `app.getInfo()` plugin API method is returning incorrect data. The `version` field contains the platform information and the `platform` field contains the version number - they appear to be swapped. Additionally, the method is now returning an array instead of an object, which breaks existing plugins that expect an object with `version` and `platform` properties.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const info = context.app.getInfo();
    console.log('Version:', info.version);  // Prints platform (e.g., "darwin")
    console.log('Platform:', info.platform); // Prints version (e.g., "2023.5.8")
  }
];
```

### Expected behavior

The method should return an object (not an array) with the correct values:
- `version` should contain the app version (e.g., "2023.5.8")
- `platform` should contain the platform (e.g., "darwin", "win32", "linux")

```js
{
  version: "2023.5.8",
  platform: "darwin"
}
```

### System Info
- Insomnia version: latest
- OS: macOS

This is breaking my plugin that relies on checking the app version for compatibility purposes.

---
Repository: /testbed
