# Bug Report

### Describe the bug

After a recent update, I'm getting unexpected behavior when working with response status codes in plugins. The `getStatusCode()` method now returns something that doesn't behave like a regular number in certain operations.

### Reproduction

```js
const statusCode = response.getStatusCode();

// This fails unexpectedly
console.log(statusCode === 200); // works fine

// But these don't work as expected:
const doubled = statusCode * 2; // NaN
const sum = statusCode + 100; // string concatenation instead of addition
const isSuccess = statusCode >= 200 && statusCode < 300; // doesn't work correctly
```

When I try to use the status code in arithmetic operations or comparisons, it doesn't behave like a number anymore. It seems like something changed with how the status code is returned.

### Expected behavior

`getStatusCode()` should return a plain number that can be used in mathematical operations and comparisons just like before. The status code should work seamlessly in conditional statements and calculations.

### System Info
- Insomnia version: latest
- Plugin context: response

This is breaking existing plugins that rely on numeric operations with status codes. Any help would be appreciated!

---
Repository: /testbed
