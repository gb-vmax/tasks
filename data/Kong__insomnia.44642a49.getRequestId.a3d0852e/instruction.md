# Bug Report

### Describe the bug

When using the plugin API to get the request ID from a response context, `getRequestId()` is now returning `undefined` instead of an empty string when there's no parent ID. This breaks existing plugins that expect a string return value.

### Reproduction

```js
const response = {
  // response without parentId
  statusCode: 200
};

const context = initResponseContext(response);
const requestId = context.getRequestId();

// requestId is now undefined instead of ''
console.log(typeof requestId); // prints 'undefined' instead of 'string'
```

### Expected behavior

`getRequestId()` should return an empty string `''` when there's no parent ID, maintaining backward compatibility with existing plugins that rely on this method always returning a string type.

### System Info
- Insomnia version: latest
- Plugin API affected: response context

---
Repository: /testbed
