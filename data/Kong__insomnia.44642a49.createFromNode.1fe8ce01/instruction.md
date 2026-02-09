# Bug Report

### Describe the bug

I'm experiencing an issue with the `Response.createFromNode()` method after a recent update. The method now throws errors for what appears to be valid response objects, breaking existing functionality.

### Reproduction

```js
const response = Response.createFromNode({
    body: 'test response',
    headers: [{ key: 'content-type', value: 'application/json' }],
    statusCode: 200,
    statusMessage: 'OK',
    elapsedTime: 150,
    originalRequest: myRequest,
    stream: Buffer.from('test')
}, []);
```

This used to work fine but now throws validation errors. The method seems to have become much stricter about what it accepts.

### Expected behavior

The method should create a Response object from the provided node response data without throwing errors for valid inputs. Previously this worked without issues.

### Additional context

This is breaking our existing API testing workflows where we construct response objects programmatically. The validation appears to be overly strict and rejects responses that should be valid.

---
Repository: /testbed
