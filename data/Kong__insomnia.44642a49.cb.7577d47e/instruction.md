# Bug Report

### Describe the bug

The `unset()` method in CookieJar is not working correctly. When trying to remove a cookie by name, the cookie is not being deleted from the jar.

### Reproduction

```js
const jar = new CookieJar();

// Set a cookie first
jar.set('https://example.com', 'session_id=abc123', (err) => {
  // Now try to unset it
  jar.unset('https://example.com', 'session_id', (err) => {
    // Cookie should be removed, but it's still there
    jar.get('https://example.com', (err, cookies) => {
      console.log(cookies); // Still shows the cookie
    });
  });
});
```

### Expected behavior

After calling `unset()` with a valid URL and cookie name, the cookie should be removed from the jar. Subsequent calls to `get()` should not return the deleted cookie.

### Additional context

This appears to have broken recently. The unset method is supposed to delete cookies but they remain in the jar after the operation completes.

---
Repository: /testbed
