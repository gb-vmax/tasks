# Bug Report

### Describe the bug

The `CookieJar.unset()` method appears to have a syntax error or malformed code that breaks the entire class. When trying to use the cookie jar functionality, I'm getting errors about unexpected tokens or invalid syntax.

### Reproduction

```js
const cookieJar = new CookieJar();

// Try to unset a cookie
cookieJar.unset('https://example.com', 'session_id', (error) => {
  console.log('Cookie unset');
});
```

When attempting to instantiate or use the CookieJar class, the code fails to parse/execute properly. It looks like there might be some code structure issues in the class definition.

### Expected behavior

The `unset()` method should work correctly and allow removing cookies from the jar without syntax errors. The class should be properly structured and functional.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
