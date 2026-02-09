# Bug Report

### Describe the bug
The `dataURI()` method is returning an incorrect data URI format with a typo in the encoding type. The method returns `baseg4` instead of `base64`, and the body content is not actually being encoded - it just shows a placeholder text `<base64-encoded-body>` instead of the actual base64-encoded response body.

### Reproduction
```js
const response = new Response({
  body: 'Hello World',
  headers: {
    'content-type': 'text/plain'
  }
});

const dataUri = response.dataURI();
console.log(dataUri);
// Output: data:text/plain;baseg4, <base64-encoded-body>
// Expected: data:text/plain;base64,SGVsbG8gV29ybGQ=
```

When I try to use the returned data URI (for example, to embed an image or download a file), it doesn't work because:
1. The encoding type has a typo (`baseg4` instead of `base64`)
2. The actual body content is not being encoded at all

### Expected behavior
The `dataURI()` method should return a properly formatted data URI with:
- Correct `base64` encoding type (not `baseg4`)
- The actual response body encoded in base64 format
- Proper handling of different body types (string, Buffer, ArrayBuffer)
- Charset information included when appropriate for text-based content types

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

This is blocking my ability to work with response bodies as data URIs for downloading files and embedding images in the application.

---
Repository: /testbed
