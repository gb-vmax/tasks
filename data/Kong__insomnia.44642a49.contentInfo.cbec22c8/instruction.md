# Bug Report

### Describe the bug

I'm experiencing an issue with the `contentInfo()` method when parsing response headers. When a `Content-Type` header is present with a valid MIME type but no additional directives (like charset), the method throws an error instead of returning the content information.

### Reproduction

```js
const response = new Response({
  headers: [
    { key: 'Content-Type', value: 'application/json' }
  ],
  body: '{"test": "data"}'
});

// This throws an error
const info = response.contentInfo();
```

The error message is: `contentInfo: header Content-Type value is blank`

### Expected behavior

The method should successfully parse the Content-Type header and return the content information with the MIME type set to `application/json` and default values for other fields. A Content-Type header with just a MIME type and no additional directives is perfectly valid according to HTTP specifications.

### Additional context

This seems to affect any response that has a Content-Type header without extra directives like `charset` or `boundary`. For example:
- `Content-Type: application/json` - fails
- `Content-Type: text/html` - fails  
- `Content-Type: application/json; charset=utf-8` - works fine

---
Repository: /testbed
