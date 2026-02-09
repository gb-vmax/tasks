# Bug Report

### Describe the bug

When passing a URL object without an `href` property to functions that expect URL parameters, the error handling doesn't work as expected. Instead of throwing a clear error message about the missing URL, the code tries to process invalid URL objects which leads to unexpected behavior.

### Reproduction

```js
// Passing an empty object as URL
const urlObj = {};
const result = toUrlObject(urlObj);
// Expected: Error thrown with message 'Request URL is not specified'
// Actual: Object is wrapped incorrectly, no error is thrown

// Passing an object without href
const urlObj2 = { protocol: 'https' };
const result2 = toUrlObject(urlObj2);
// Expected: Error thrown
// Actual: No error, invalid URL object is created
```

### Expected behavior

The function should throw an error with the message "Request URL is not specified" when:
- An empty object is passed
- An object without an `href` property is passed
- Any falsy value is passed

### System Info
- Package: insomnia-sdk
- Version: latest

This is causing issues in our URL validation logic where we expect proper error handling for invalid URL inputs.

---
Repository: /testbed
