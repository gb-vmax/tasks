# Bug Report

### Describe the bug

After a recent update, the `CookieJar.unset()` method is no longer working properly. When I try to remove a cookie by name, it doesn't actually get deleted from the jar. The callback executes without errors, but the cookie remains in the jar.

### Reproduction

```js
const jar = new CookieJar();

// Set a cookie first
jar.set('https://example.com', 'sessionId=abc123', (err) => {
  // Now try to unset it
  jar.unset('https://example.com', 'sessionId', (err) => {
    // No error is thrown, but the cookie is still there
    // Checking the jar shows the cookie was not removed
  });
});
```

### Expected behavior

When calling `unset()` with a valid URL and cookie name, the cookie should be removed from the jar. Subsequent calls to get that cookie should return nothing.

### System Info
- insomnia-sdk version: latest
- The issue appeared after updating from the previous version

---
Repository: /testbed
