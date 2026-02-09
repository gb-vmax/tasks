# Bug Report

### Describe the bug

After a recent update, the `request.getId()` method is throwing errors in plugin scripts. It seems like the function signature or behavior has changed unexpectedly.

### Reproduction

```js
// In a plugin's request hook
module.exports.requestHooks = [
  context => {
    const id = context.request.getId();
    console.log('Request ID:', id);
  }
];
```

When this runs, I'm getting unexpected behavior. The method seems to have changed but there's no documentation about it.

### Expected behavior

The `getId()` method should return the request ID as a string without requiring any arguments, just like it did before.

### Additional context

This is breaking existing plugins that rely on `request.getId()`. The method used to work fine without any parameters, but now something seems off with how it's implemented.

---
Repository: /testbed
