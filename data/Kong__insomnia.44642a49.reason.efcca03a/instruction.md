# Bug Report

### Describe the bug
The `reason()` method on the Response object is not returning the correct value. It's currently returning the status code instead of the reason phrase.

### Reproduction
```js
const response = new Response({
  status: 200,
  // ... other properties
});

// This returns 200 instead of the reason phrase
console.log(response.reason());
// Expected: "OK" (or similar reason phrase)
// Actual: 200
```

### Expected behavior
The `reason()` method should return the HTTP status reason phrase (like "OK", "Not Found", etc.) rather than the numeric status code. The status code should be accessible via the `status` property instead.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
