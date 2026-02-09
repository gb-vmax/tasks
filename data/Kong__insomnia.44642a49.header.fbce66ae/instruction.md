# Bug Report

### Describe the bug

I'm having an issue with the `response.to.not.have.header()` assertion method. When checking that a response does NOT have a specific header with a value (using the `header: value` format), the assertion is not working correctly.

### Reproduction

```js
// Response has header: Content-Type: application/json

// This should pass but fails
response.to.not.have.header('Content-Type: text/html');

// Expected: assertion passes (response doesn't have Content-Type: text/html)
// Actual: assertion behavior is incorrect
```

The problem occurs when using the colon-separated format (`Header-Name: value`) with the `.not.have.header()` assertion. It seems like the negation logic isn't being applied properly when both header name and value are specified.

### Expected behavior

When using `response.to.not.have.header('Header-Name: value')`, the assertion should pass if:
- The header doesn't exist, OR
- The header exists but has a different value

Currently it's not behaving as expected when the header exists with a different value.

### System Info
- insomnia-sdk version: latest
- Using the response assertion API

---
Repository: /testbed
