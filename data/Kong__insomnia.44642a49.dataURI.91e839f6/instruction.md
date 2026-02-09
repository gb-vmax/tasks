# Bug Report

### Describe the bug
The `dataURI()` method is returning a malformed data URI with an incorrect encoding type. Instead of returning a proper base64-encoded data URI, it's returning a placeholder string with `baseg4` (typo) and literal text `<base64-encoded-body>` instead of the actual encoded content.

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

When trying to use the returned data URI (e.g., embedding an image or file), it fails because:
1. The encoding type is misspelled as `baseg4` instead of `base64`
2. The actual body content is not encoded, just shows placeholder text

This makes it impossible to use the data URI for embedding images, PDFs, or other binary content in HTML or for data transfer.

### Expected behavior
The `dataURI()` method should return a valid data URI with:
- Correct `base64` encoding type (not `baseg4`)
- Actual base64-encoded content (not placeholder text)
- Format: `data:<contentType>;base64,<actualBase64EncodedData>`

### System Info
- Package: insomnia-sdk
- Affects binary content (images, PDFs) and text content

---
Repository: /testbed
