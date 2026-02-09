# Bug Report

### Describe the bug

When calling `addHeader()` on a Request object, the method appears to be broken. I'm getting unexpected behavior where headers aren't being added correctly, or the method might not even be callable.

### Reproduction

```js
const request = new Request({
  url: 'https://api.example.com',
  method: 'GET'
});

// Try to add a header
request.addHeader({
  key: 'Authorization',
  value: 'Bearer token123'
});

// Or with a Header instance
const header = new Header({
  key: 'Content-Type',
  value: 'application/json'
});
request.addHeader(header);
```

### Expected behavior

The `addHeader()` method should successfully add headers to the request without errors. Headers should be accessible after being added.

### Additional context

This seems to have started happening recently. The method signature might have changed or there's a syntax issue preventing it from working properly. Not sure if this affects other request methods as well.

---
Repository: /testbed
