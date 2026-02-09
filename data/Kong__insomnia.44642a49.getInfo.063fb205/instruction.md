# Bug Report

### Describe the bug
The `app.getInfo()` plugin API is returning incorrect values. The `version` and `platform` fields appear to be swapped or concatenated incorrectly.

### Reproduction
```js
// In a plugin
module.exports.requestHooks = [
  context => {
    const info = context.app.getInfo();
    console.log('Version:', info.version);
    console.log('Platform:', info.platform);
  }
];
```

When I call `app.getInfo()`, I'm getting unexpected results:
- The `version` field contains what looks like a concatenated string with both version and platform
- The `platform` field contains the version number instead of the platform name

### Expected behavior
The method should return:
```js
{
  version: '2023.5.0',  // actual version string
  platform: 'darwin'     // actual platform string
}
```

But instead it's returning something like:
```js
{
  version: '2023.5.0-darwin',  // concatenated?
  platform: '2023.5.0'          // this should be platform, not version
}
```

This is breaking plugins that rely on checking the platform or version separately.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
