# Bug Report

### Describe the bug

The `CookieJar.unset()` method crashes when trying to delete a cookie from a URL that doesn't exist in the jar. After calling `unset()` with a URL that has no associated cookies, the method attempts to call `.delete()` on an undefined object, causing a runtime error.

### Reproduction

```js
const jar = new CookieJar();

// Try to unset a cookie for a URL that was never set
jar.unset('https://example.com', 'sessionId', (error) => {
  console.log('Callback should be called');
});
```

### Expected behavior

The callback should be invoked without errors even when trying to unset a cookie from a URL that doesn't exist in the jar. The method should handle this case gracefully and just call the callback with no error.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
