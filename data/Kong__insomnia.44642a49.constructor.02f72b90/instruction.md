# Bug Report

### Describe the bug

After a recent update, the `Response` object constructor appears to be broken or incomplete. When trying to create a new Response instance, the initialization fails because the constructor implementation was removed or not properly finished.

### Reproduction

```js
const response = new Response({
  body: 'test response',
  code: 200,
  header: [
    { key: 'Content-Type', value: 'application/json' }
  ],
  cookie: []
});

// This throws an error or doesn't initialize properly
console.log(response.body); // undefined or error
console.log(response.code); // undefined or error
```

### Expected behavior

The Response object should be properly initialized with all the provided options (body, code, headers, cookies, etc.). The constructor should set up all the necessary properties and return a working Response instance.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This seems like the constructor implementation got accidentally removed or wasn't completed during a refactoring. The helper functions `normalizeHeaderName` and `extractResponseMetadata` are defined but the actual constructor logic is missing.

---
Repository: /testbed
