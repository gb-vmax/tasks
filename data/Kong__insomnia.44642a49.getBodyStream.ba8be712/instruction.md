# Bug Report

### Describe the bug

After a recent update, the `getBodyStream()` method in the plugin response context is broken. When trying to call it without any arguments (which should be the default behavior), I'm getting syntax errors or the method doesn't work as expected.

### Reproduction

```js
// In a plugin response hook
const stream = response.getBodyStream();
// This fails or throws an error
```

The method used to work fine when called without parameters, but now it seems like something is wrong with the function definition.

### Expected behavior

`getBodyStream()` should work when called without any arguments, just like before. It should return the response body stream without requiring any options to be passed.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our plugin from working correctly. Any help would be appreciated!

---
Repository: /testbed
