# Bug Report

### Describe the bug

I'm encountering a syntax error when trying to use the CookieJar's `unset` method. The code appears to have malformed syntax that prevents it from running properly.

### Reproduction

```js
const cookieJar = new CookieJar();

// Attempting to unset a cookie results in a syntax error
cookieJar.unset('https://example.com', 'myCookie', (error) => {
  if (error) {
    console.error('Error:', error);
  }
});
```

### Expected behavior

The `unset` method should execute without syntax errors and properly remove the specified cookie from the jar.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
