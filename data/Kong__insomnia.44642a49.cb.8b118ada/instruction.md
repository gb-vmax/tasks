# Bug Report

### Describe the bug

The `CookieJar.unset()` method appears to have a syntax error or malformed code structure. When trying to use the cookie jar to remove cookies, the application fails to compile or run properly.

### Reproduction

```js
const cookieJar = new CookieJar();

// Set a cookie first
cookieJar.set('https://example.com', 'session_id=abc123', (err) => {
  // Try to unset the cookie
  cookieJar.unset('https://example.com', 'session_id', (err) => {
    console.log('Cookie removed');
  });
});
```

### Expected behavior

The cookie should be removed successfully and the callback should be invoked without errors. The code should compile and run without any syntax issues.

### System Info

- Package: insomnia-sdk
- Affected file: `packages/insomnia-sdk/src/objects/cookies.ts`

The issue seems to be in the `unset` method implementation. The code structure looks broken and there appears to be misplaced private fields and methods inside the function body.

---
Repository: /testbed
