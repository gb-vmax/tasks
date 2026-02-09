# Bug Report

### Describe the bug

After a recent update, the SDK is returning `undefined` for responses when request errors occur, instead of providing error details. This makes it impossible to handle and debug failed requests properly in scripts.

Previously, when a request failed (timeout, DNS error, SSL issues, etc.), we could still access some response information. Now the response object is just `undefined` and there's no way to determine what went wrong.

### Reproduction

```js
// Make a request that will fail (e.g., invalid hostname)
const response = await insomnia.send({
  url: 'https://this-domain-definitely-does-not-exist-12345.com',
  method: 'GET'
});

// response is undefined instead of containing error information
console.log(response); // undefined
// Expected: some response object with error details
```

Similar issue happens with:
- Timeout errors
- SSL/certificate errors  
- Connection refused errors
- DNS resolution failures

### Expected behavior

When a request fails, the response object should still be returned with error information so scripts can handle different error types appropriately. For example, we should be able to check status codes, error messages, or custom headers to determine what went wrong.

### System Info
- Insomnia SDK version: latest
- OS: macOS

This is blocking our ability to write proper error handling in pre-request and test scripts. Any workaround would be appreciated!

---
Repository: /testbed
