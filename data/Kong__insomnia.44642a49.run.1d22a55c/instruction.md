# Bug Report

### Describe the bug

I'm experiencing an issue with the base64 template tag where the encoding/decoding seems to be broken. When I try to use the base64 tag in my templates, the application crashes or produces incorrect output.

### Reproduction

```js
// Using the base64 template tag with URL-safe encoding
{% base64 'encode', 'url', 'Hello World' %}

// Or trying to decode base64 data
{% base64 'decode', 'normal', 'SGVsbG8gV29ybGQ=' %}
```

### Expected behavior

The base64 tag should properly encode and decode text in different formats (normal, url, hex) without errors. The encoded output should be valid base64 and decoding should return the original text.

### System Info

- Insomnia version: latest
- OS: macOS

This appears to have started happening recently, possibly after a recent update. The template tag was working fine before.

---
Repository: /testbed
