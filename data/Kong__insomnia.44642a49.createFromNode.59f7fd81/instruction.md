# Bug Report

### Describe the bug

I'm encountering an issue with the `Response.createFromNode()` method after a recent update. The method appears to have been removed or relocated, causing errors when trying to create Response objects from node response data.

### Reproduction

```js
const response = Response.createFromNode(
  {
    body: 'test response',
    headers: [{ key: 'Content-Type', value: 'application/json' }],
    statusCode: 200,
    statusMessage: 'OK',
    elapsedTime: 150,
    originalRequest: myRequest,
    stream: Buffer.from('test')
  },
  []
);
```

This code was working before but now throws an error saying `createFromNode` is not a function or is undefined.

### Expected behavior

The `createFromNode()` static method should be available on the Response class and successfully create a Response instance from the provided node response data and cookies.

### Additional context

This seems to have broken after updating to the latest version. The method was previously a static method on the Response class and was used throughout our codebase for converting node-style responses to Response objects.

---
Repository: /testbed
