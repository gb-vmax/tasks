# Bug Report

### Describe the bug

When trying to unset a cookie using `CookieJar.unset()`, the method appears to be broken. The callback is never invoked and the cookie is not removed from the jar.

### Reproduction

```js
const jar = new CookieJar();

// Set a cookie first
jar.set('https://example.com', 'sessionId=abc123', (err) => {
  // Try to unset it
  jar.unset('https://example.com', 'sessionId', (error) => {
    // This callback is never called
    console.log('Callback invoked:', error);
  });
});
```

### Expected behavior

The `unset` method should:
1. Remove the specified cookie from the jar
2. Invoke the callback with `undefined` (no error) when successful
3. Invoke the callback with an error if the cookie doesn't exist

### Current behavior

The callback is not being invoked at all, and the cookie remains in the jar. The method seems to have a syntax/logic error that prevents it from executing properly.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
