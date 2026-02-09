# Bug Report

### Describe the bug

The Response object constructor appears to be completely broken. When trying to create a new Response instance, I'm getting syntax errors or the object is not being initialized properly at all.

### Reproduction

```js
const response = new Response({
  code: 200,
  body: 'test response',
  header: [{ key: 'Content-Type', value: 'application/json' }],
  responseTime: 150
});

console.log(response.code); // Should print 200
console.log(response.body); // Should print 'test response'
```

### Expected behavior

The Response object should be created successfully with all properties properly initialized (code, body, headers, cookies, status, etc.). The constructor should handle the options parameter and set up all the necessary fields.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This is blocking my ability to work with response objects in the SDK. Any help would be appreciated!

---
Repository: /testbed
