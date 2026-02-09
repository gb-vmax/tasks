# Bug Report

### Describe the bug

After a recent update, cookie domains are being automatically modified in unexpected ways. When I set a cookie with a domain that includes a protocol prefix (like `http://` or `https://`), the protocol gets stripped out. Additionally, domains are being forced to lowercase and ports are being removed.

This is causing issues with cookies that were previously stored with uppercase letters or specific port numbers in their domain field.

### Reproduction

```js
// Create a cookie jar with cookies that have various domain formats
const cookieJar = {
  cookies: [
    {
      domain: 'HTTP://Example.COM',
      // ... other cookie properties
    },
    {
      domain: 'api.example.com:8080',
      // ... other cookie properties
    }
  ]
};

// After migration, domains are changed:
// 'HTTP://Example.COM' becomes 'example.com'
// 'api.example.com:8080' becomes 'api.example.com'
```

### Expected behavior

Cookie domains should be preserved as-is, or at minimum, the normalization behavior should be documented. The automatic stripping of protocols, ports, and case conversion is breaking existing cookie storage.

### Additional context

This also affects other cookie properties:
- `path` is being automatically set to '/' if undefined or empty
- `secure` and `httpOnly` are being forced to `false` if not boolean
- `expires` values are being validated and potentially nullified

These automatic transformations are causing cookies to behave differently than expected, especially when importing cookies from other sources or working with legacy cookie data.

---
Repository: /testbed
