# Bug Report

### Describe the bug
The `app.getInfo()` plugin API method is returning swapped values for `version` and `platform`. When I call this method from a plugin, the version field contains the platform information and the platform field contains the version information.

### Reproduction
```js
const info = context.app.getInfo();
console.log('Version:', info.version);  // Prints platform (e.g., "darwin", "win32")
console.log('Platform:', info.platform); // Prints version (e.g., "2023.5.8")
```

### Expected behavior
The method should return:
- `version`: The application version string
- `platform`: The platform identifier (darwin, win32, linux, etc.)

Currently these values are reversed.

### System Info
- Insomnia version: Latest
- OS: macOS

This is breaking plugins that rely on checking the app version or platform for compatibility checks.

---
Repository: /testbed
