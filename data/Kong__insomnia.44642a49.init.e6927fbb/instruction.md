# Bug Report

### Describe the bug

After a recent update, cookie jars are being initialized with `null` cookies instead of an empty array. This causes errors when trying to access or manipulate cookies since the code expects an array but gets `null` instead.

### Reproduction

```js
const jar = init();
// Expected: jar.cookies should be []
// Actual: jar.cookies is null

// This will throw an error
jar.cookies.forEach(cookie => {
  console.log(cookie);
});
```

### Expected behavior

The `init()` function should return a cookie jar object with `cookies` initialized as an empty array `[]`, not `null`. This way array methods can be safely used without null checks.

### Additional context

This breaks existing code that assumes `cookies` is always an array. Operations like `push`, `filter`, `map` etc. on the cookies property now fail with "Cannot read property of null" errors.

---
Repository: /testbed
