# Bug Report

### Describe the bug

After updating the plugin API, the `getUrl()` method is throwing a syntax error when trying to retrieve the request URL. The plugin context seems to have broken functionality for accessing request URLs.

### Reproduction

```js
// In a plugin
module.exports.requestHooks = [
  context => {
    // This throws an error
    const url = context.request.getUrl();
    console.log(url);
  }
];
```

### Expected behavior

The `getUrl()` method should return the full request URL without errors, just like it did in previous versions.

### System Info
- Insomnia version: latest
- OS: Multiple platforms affected

This seems to have started after a recent update to the request context. The method was working fine before but now fails completely.

---
Repository: /testbed
