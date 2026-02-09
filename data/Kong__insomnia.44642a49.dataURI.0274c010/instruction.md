# Bug Report

### Describe the bug

The `dataURI()` method is returning a malformed data URI with incorrect encoding. The generated data URI contains `baseg4` instead of `base64` and includes placeholder text `<base64-encoded-body>` instead of the actual encoded body content.

### Reproduction

```js
const response = new Response({
  body: 'Hello World',
  contentType: 'text/plain'
});

const dataUri = response.dataURI();
console.log(dataUri);
// Output: data:text/plain;baseg4, <base64-encoded-body>
// Expected: data:text/plain;base64,SGVsbG8gV29ybGQ=
```

### Expected behavior

The method should return a properly formatted data URI with:
1. Correct `base64` encoding specification (not `baseg4`)
2. Actual base64-encoded body content instead of placeholder text
3. Proper comma separator between encoding and data

The data URI should be usable in contexts like embedding images or other resources inline.

### System Info
- insomnia-sdk version: latest
- Node.js version: 18.x

---
Repository: /testbed
