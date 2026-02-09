# Bug Report

### Describe the bug

The `reason()` method on Response objects is returning the status code instead of the reason phrase. When I call `response.reason()`, I expect to get a string like "OK" or "Not Found", but instead I'm getting the numeric status code.

### Reproduction

```js
const response = // ... get response object

// This returns 200 instead of "OK"
console.log(response.reason());

// Expected: "OK"
// Actual: 200
```

### Expected behavior

The `reason()` method should return the HTTP reason phrase (e.g., "OK", "Not Found", "Internal Server Error") corresponding to the status code, not the status code itself.

### Additional context

This seems like it might be a regression - the method name suggests it should return a reason phrase, but the current implementation just returns `this.status` which is the numeric code.

---
Repository: /testbed
