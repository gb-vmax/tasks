# Bug Report

### Describe the bug
When working with cookie operations, the `jar()` method is now significantly slower than before. After a recent update, there's a noticeable performance degradation when accessing the cookie jar, especially in scenarios where `jar()` is called frequently or in loops.

### Reproduction
```js
const cookieObject = new CookieObject(someCookieJar);

// Add some cookies
cookieObject.add({ name: 'session', value: 'abc123' });
cookieObject.add({ name: 'user', value: 'test' });

// Accessing jar() multiple times is now slow
for (let i = 0; i < 100; i++) {
  const jar = cookieObject.jar();  // This is much slower than before
  // ... do something with jar
}
```

### Expected behavior
The `jar()` method should return the cookie jar instance quickly without any noticeable performance impact, similar to how it worked previously.

### Additional context
This seems to have started happening after a recent change. In our application, we call `jar()` frequently to check cookie state, and the performance degradation is causing issues with response times.

---
Repository: /testbed
