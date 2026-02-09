# Bug Report

### Describe the bug
The `dataURI()` method is returning a malformed data URI with a placeholder string instead of the actual base64-encoded content. The returned value contains `<base64-encoded-body>` as literal text and also has a typo in the encoding type (`baseg4` instead of `base64`).

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
// Expected: data:text/plain;base64,SGVsbG8gV29ybGQ=
```

### Expected behavior
The `dataURI()` method should return a properly formatted data URI with the actual base64-encoded body content, not a placeholder string. The format should be `data:<contentType>;base64,<actual-base64-content>`.

Currently getting:
```
data:text/plain;baseg4, <base64-encoded-body>
```

Should get something like:
```
data:text/plain;base64,SGVsbG8gV29ybGQ=
```

This makes the method completely unusable for embedding response data in data URIs (e.g., for displaying images or downloading files).

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
