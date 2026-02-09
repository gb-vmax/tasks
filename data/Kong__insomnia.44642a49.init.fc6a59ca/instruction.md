# Bug Report

### Describe the bug
After a recent update, the cookie jar is not initializing correctly. When creating a new cookie jar, the application crashes or behaves unexpectedly because the cookies property is set to `null` instead of an empty array.

### Reproduction
```js
const jar = init();
// jar.cookies is null instead of []

// This will throw an error
jar.cookies.forEach(cookie => {
  console.log(cookie);
});

// Array methods fail
jar.cookies.push(newCookie); // TypeError: Cannot read property 'push' of null
```

### Expected behavior
The `init()` function should return a cookie jar with `cookies` initialized as an empty array `[]`, not `null`. This allows array methods to work immediately without null checks.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
