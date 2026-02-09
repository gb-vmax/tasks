# Bug Report

### Describe the bug

The `reason()` method on Response objects is returning unexpected values. When I call `response.reason()` without any arguments, it's still returning just the status phrase as before, but the method signature seems to have changed to accept format parameters.

### Reproduction

```js
const response = // ... get response object

// This used to work and return the status phrase
const reason = response.reason();
console.log(reason); // Expected: status phrase like "OK" or "Not Found"

// But now trying different formats gives inconsistent results
const reasonCode = response.reason('code');
const reasonBoth = response.reason('both');
```

### Expected behavior

The `reason()` method should consistently return the HTTP status reason phrase (like "OK", "Not Found", etc.) when called without arguments, matching the previous behavior. If format options are being added, they should be documented and work as expected.

### System Info
- insomnia-sdk version: latest
- The issue appeared after a recent update to the response object handling

---
Repository: /testbed
