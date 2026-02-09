# Bug Report

### Describe the bug

I'm experiencing an issue with the response header assertions in the SDK. When trying to check if a response header exists with a specific value, the assertion is not working as expected. It seems like the header value comparison is not being performed correctly.

### Reproduction

```js
// Trying to assert that a response has a Content-Type header with value 'application/json'
pm.response.to.have.header('Content-Type', 'application/json');

// Expected: assertion should pass if header exists with matching value
// Actual: behavior is inconsistent or not working
```

The issue occurs when passing a second parameter (expected value) to the `header` assertion. Without the second parameter, checking for header existence works fine, but when trying to validate the header's value, things break down.

### Expected behavior

The assertion should:
1. Check if the header exists (case-insensitive)
2. If an expected value is provided, verify the header's value matches (case-insensitive)
3. Pass the assertion if both conditions are met

### Additional context

This seems to have started happening recently. The basic header existence check (without value comparison) still works:
```js
pm.response.to.have.header('Content-Type'); // This works
```

But adding the value parameter causes issues:
```js
pm.response.to.have.header('Content-Type', 'application/json'); // This doesn't work correctly
```

---
Repository: /testbed
