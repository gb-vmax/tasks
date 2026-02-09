# Bug Report

### Describe the bug
After a recent update, the `getStatusCode()` method is returning an object instead of a number when called without arguments. This breaks existing plugins that expect a numeric status code.

### Reproduction
```js
const response = {
  statusCode: 200,
  // ... other response properties
};

// This used to return 200 (number)
// Now returns an object with code, category, isValid, wasNormalized properties
const statusCode = response.getStatusCode();

// Breaks code that does numeric comparisons
if (statusCode === 200) {
  // This condition never matches anymore
}
```

### Expected behavior
Calling `getStatusCode()` without any arguments should return a numeric status code (e.g., `200`, `404`, `500`) just like it did before, maintaining backwards compatibility with existing plugins.

### Additional context
It looks like the method signature changed to accept an optional `detailed` parameter, but the default behavior when called without arguments should still return the simple numeric code to avoid breaking existing integrations.

---
Repository: /testbed
