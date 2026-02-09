# Bug Report

### Describe the bug
When calling `response.text()` on a Response object, it returns the string `"true"` or `"false"` instead of the actual response body content.

### Reproduction
```js
// Make a request that returns some text
const response = await insomnia.send();

// Expected: the actual response body as a string (e.g., "Hello World", JSON string, etc.)
// Actual: returns "true" or "false"
console.log(response.text());
```

### Expected behavior
The `text()` method should return the response body as a string, not a boolean value converted to string. For example, if the API returns `{"message": "success"}`, calling `response.text()` should return that JSON string, not `"true"`.

### System Info
- insomnia-sdk version: latest

---
Repository: /testbed
