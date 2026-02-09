# Bug Report

### Describe the bug

I'm encountering an issue when trying to add headers to a request object. After a recent update, the `addHeader` method appears to be broken and causes the application to fail.

### Reproduction

```js
const request = new Request({
  url: 'https://api.example.com',
  method: 'GET'
});

// This causes an error
request.addHeader({
  key: 'Content-Type',
  value: 'application/json'
});
```

### Expected behavior

The header should be added to the request without any errors. Previously this worked fine, but now it seems like there's a syntax issue preventing the method from executing properly.

### Additional context

This started happening after the latest changes. The method seems incomplete or has some kind of parsing error. Can't proceed with any request operations that require adding headers.

---
Repository: /testbed
