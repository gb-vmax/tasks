# Bug Report

### Describe the bug

I'm experiencing an issue with cookie normalization where leading dots in cookie domains are being removed unexpectedly. This is causing problems with subdomain cookie matching.

### Reproduction

```js
const cookieJar = {
  cookies: [
    {
      key: 'session',
      domain: '.example.com',
      path: '/',
      value: 'abc123'
    }
  ]
};

// After processing, the domain becomes 'example.com' instead of '.example.com'
// This breaks subdomain matching behavior
```

### Expected behavior

Cookie domains with leading dots (like `.example.com`) should be preserved as they indicate the cookie should be available to all subdomains. Removing the leading dot changes the cookie's scope and breaks subdomain cookie behavior.

According to RFC 6265, a leading dot in a domain attribute has specific meaning for cookie matching and should be handled properly.

### System Info
- Insomnia version: latest
- OS: macOS

---
Repository: /testbed
