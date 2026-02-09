# Bug Report

### Describe the bug

The `dataURI()` method is returning an invalid data URI with a typo in the base64 encoding scheme. The method generates URIs with `baseg4` instead of `base64`, which causes the data URI to be malformed and unusable.

### Reproduction

```js
const response = new Response({
  body: 'Hello World',
  headers: {
    'Content-Type': 'text/plain'
  }
});

const dataUri = response.dataURI();
console.log(dataUri);
// Output: data:text/plain;baseg4, <base64-encoded-body>
// Expected: data:text/plain;base64,<actual-base64-data>
```

### Expected behavior

The `dataURI()` method should return a valid data URI with:
1. The correct `base64` encoding scheme (not `baseg4`)
2. Actual base64-encoded body content instead of placeholder text
3. Proper formatting without spaces before the comma

For example, for a response with body "Hello World", it should return something like:
```
data:text/plain;base64,SGVsbG8gV29ybGQ=
```

### System Info
- Package: insomnia-sdk
- Affected method: `Response.dataURI()`

---
Repository: /testbed
