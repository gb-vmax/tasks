# Bug Report

### Describe the bug

After a recent update, the Cookie constructor is broken and throws an error when trying to create cookie objects. The application crashes immediately when attempting to instantiate a Cookie with either a string or object definition.

### Reproduction

```js
// This used to work but now fails
const cookie1 = new Cookie('sessionId=abc123; Domain=example.com; Path=/');

// This also fails
const cookie2 = new Cookie({
  name: 'sessionId',
  value: 'abc123',
  domain: 'example.com',
  path: '/'
});
```

Both approaches result in an error and the Cookie object is never created. The constructor seems to be failing before any parsing or validation can occur.

### Expected behavior

Cookie objects should be created successfully from both string and object definitions, just like they did in previous versions.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
