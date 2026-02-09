# Bug Report

### Describe the bug
When using certificates with URL matching, the `canApplyTo()` method is not working correctly. It seems to always return true for certificates without a matches pattern, and when there is a matches pattern, it's not properly checking against the provided URL.

### Reproduction
```js
const cert = new Certificate({
  name: 'test-cert',
  matches: /^https:\/\/api\.example\.com/,
  // ... other cert options
});

// This should return true
console.log(cert.canApplyTo('https://api.example.com/users'));

// This should return false
console.log(cert.canApplyTo('https://other-domain.com/api'));
```

### Expected behavior
- When a certificate has a `matches` pattern, `canApplyTo(url)` should test the provided URL against that pattern
- When a certificate has no `matches` pattern, it should return false (not apply to any URL)
- The method should correctly validate whether the certificate should be applied to a given URL

### Current behavior
The URL matching logic doesn't seem to be comparing the right values, causing certificates to either apply incorrectly or not apply when they should.

### System Info
- insomnia-sdk version: latest
- Platform: All

---
Repository: /testbed
