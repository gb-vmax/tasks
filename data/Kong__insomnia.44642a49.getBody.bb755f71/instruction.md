# Bug Report

### Describe the bug

The `getBody()` method in the response context plugin is not working as expected after a recent update. When calling `getBody()` without any arguments, it returns `undefined` instead of the response body buffer.

### Reproduction

```js
// In a plugin script
const response = await insomnia.send(request);

// This now returns undefined instead of the body buffer
const body = response.getBody();
console.log(body); // undefined
```

### Expected behavior

When calling `getBody()` without arguments, it should return the response body buffer by default, maintaining backward compatibility with existing plugins.

### Additional context

This appears to have broken after changes to support format parameters. The method signature changed but the default behavior when no format is specified doesn't match the previous implementation.

Existing plugins that rely on `getBody()` returning the buffer are now broken.

---
Repository: /testbed
