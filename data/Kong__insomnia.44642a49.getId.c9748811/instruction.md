# Bug Report

### Describe the bug

I'm experiencing an issue with the `request.getId()` method in the plugin context. After a recent update, calling `getId()` is throwing an error about `this._idCache` being undefined.

### Reproduction

```js
const request = context.request;

// This throws an error
const id = request.getId();
```

The error occurs when trying to access the request ID through the plugin context API. It seems like the method is trying to reference `this._idCache` but it's not being initialized anywhere.

### Expected behavior

The `getId()` method should return the request ID without throwing any errors, just like it did before.

### Additional context

This started happening after updating to the latest version. The method used to work fine and simply returned `renderedRequest._id`. Now it's trying to use some caching mechanism but the cache object doesn't exist on the context.

---
Repository: /testbed
