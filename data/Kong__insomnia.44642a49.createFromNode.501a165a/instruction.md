# Bug Report

### Describe the bug

After a recent update, the Response object creation seems to be broken. When trying to create a Response from node data, I'm getting errors about missing methods or undefined behavior.

### Reproduction

```js
const responseData = {
    body: 'test response body',
    headers: [
        { key: 'Content-Type', value: 'application/json' },
        { key: 'Content-Length', value: '123' }
    ],
    statusCode: 200,
    statusMessage: 'OK',
    elapsedTime: 150,
    originalRequest: myRequest,
    stream: Buffer.from('test')
};

const cookies = [
    { name: 'session', value: 'abc123' }
];

// This fails - createFromNode is not found or doesn't work as expected
const response = Response.createFromNode(responseData, cookies);
```

### Expected behavior

The `Response.createFromNode()` static method should create a Response object from the provided node response data and cookies, as it did in previous versions.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
