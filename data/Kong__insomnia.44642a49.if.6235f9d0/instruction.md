# Bug Report

### Describe the bug

After a recent update, the script response handling appears to be broken. When a request fails (timeout, connection error, DNS issues, etc.), the response object is now `undefined` instead of returning an error response object that can be inspected in scripts.

### Reproduction

```js
// Pre-request or test script
pm.sendRequest({
  url: 'http://invalid-domain-that-does-not-exist.local',
  method: 'GET'
}, function (err, response) {
  console.log(response); // This is now undefined
  // Previously we could check response.code or response.status
});
```

Also happens with timeout scenarios:

```js
pm.sendRequest({
  url: 'http://httpstat.us/200?sleep=60000',
  timeout: 1000
}, function (err, response) {
  console.log(response); // undefined - can't check if it was a timeout
});
```

### Expected behavior

The response object should be defined even when requests fail, allowing scripts to:
- Check the error type (timeout, connection error, DNS error, etc.)
- Access status codes that represent the error (504 for timeout, 502 for connection issues)
- Handle different error scenarios programmatically

Previously, failed requests would return a response object with error information that could be inspected. Now it just returns `undefined` which makes error handling in scripts impossible.

### System Info
- Insomnia SDK version: latest
- OS: macOS

---
Repository: /testbed
