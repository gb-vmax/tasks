# Bug Report

### Describe the bug

The `CookieJar.unset()` method is not calling the callback function when attempting to delete a cookie that doesn't exist. This causes the callback to never be invoked in certain scenarios, potentially leading to hanging promises or unhandled flows.

### Reproduction

```js
const cookieJar = new CookieJar();

// Try to unset a cookie that doesn't exist
cookieJar.unset('https://example.com', 'nonexistent-cookie', (error) => {
  console.log('Callback invoked:', error);
});

// Expected: Callback should be invoked
// Actual: Callback is never called if the cookie doesn't exist in the domain
```

### Expected behavior

The callback should always be invoked when `unset()` is called, regardless of whether the cookie exists or not. This is important for proper async flow control and to avoid hanging operations.

### Additional context

This seems to affect scenarios where you're trying to clean up cookies that may or may not exist. The callback should be called with `null` or `undefined` to indicate successful completion even when the cookie wasn't found.

---
Repository: /testbed
