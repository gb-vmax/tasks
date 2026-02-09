# Bug Report

### Describe the bug

The `jar()` method on `CookieObject` is not working as expected after recent changes. When I try to use it with a domain filter parameter, it's not filtering cookies correctly and sometimes returns unexpected results.

### Reproduction

```js
const cookieObject = new CookieObject();

// Add some cookies for different domains
cookieObject.add({
  key: 'session',
  value: 'abc123',
  domain: 'example.com'
});

cookieObject.add({
  key: 'token',
  value: 'xyz789',
  domain: 'api.example.com'
});

// Try to get jar filtered by domain
const jar = cookieObject.jar('*.example.com');

// Expected: jar should contain cookies from both example.com and api.example.com
// Actual: getting inconsistent results or errors
```

Also noticed that calling `jar()` without any parameters sometimes doesn't reflect the current state of cookies that were added or removed.

### Expected behavior

- `jar()` should return the current cookie jar with all cookies
- `jar(domainFilter)` should return a filtered jar containing only cookies matching the domain pattern (supporting wildcards like `*.example.com`)
- Changes to cookies (add/remove) should be reflected in the jar

### System Info
- Using insomnia-sdk
- Issue appeared after updating to latest version

---
Repository: /testbed
