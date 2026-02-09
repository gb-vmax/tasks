# Bug Report

### Describe the bug

After a recent update, the plugin API's `app.getInfo()` method is throwing a syntax error and causing plugins to fail. The method appears to be malformed and doesn't return the expected object structure.

### Reproduction

```js
// In a plugin's main function
module.exports.requestHooks = [
  context => {
    const info = context.app.getInfo();
    console.log(info); // This throws an error
  }
];
```

When trying to access `app.getInfo()` from the plugin context, the application crashes with a syntax error instead of returning the application information.

### Expected behavior

The `getInfo()` method should return an object containing version and platform information without throwing any errors:

```js
{
  version: '2023.x.x',
  platform: 'darwin' // or 'win32', 'linux', etc.
}
```

### Additional context

This seems to have broken after the last update. Previously working plugins that call `app.getInfo()` are now failing to load. The method definition in the plugin context appears to have formatting issues that prevent it from being parsed correctly.

---
Repository: /testbed
