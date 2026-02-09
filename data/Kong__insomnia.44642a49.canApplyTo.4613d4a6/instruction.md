# Bug Report

### Certificate matching logic is inverted

I've discovered an issue with certificate matching that's causing certificates to be applied incorrectly to requests.

### Reproduction
```js
const cert = new Certificate({
  name: 'My Cert',
  matches: /^https:\/\/api\.example\.com/,
  // ... other cert options
});

// This returns false when it should return true
cert.canApplyTo('https://api.example.com/users');

// And this returns true when it should return false
const certWithoutMatches = new Certificate({
  name: 'Another Cert',
  // no matches pattern defined
});
certWithoutMatches.canApplyTo('https://any-url.com');
```

### Expected behavior
- When a certificate has a `matches` pattern that matches the URL, `canApplyTo()` should return `true`
- When a certificate has no `matches` pattern, `canApplyTo()` should return `false`

### Actual behavior
The behavior appears to be completely inverted:
- Certificates with matching patterns return `false` for URLs they should match
- Certificates without patterns return `true` for any URL

This is breaking certificate selection for requests and causing the wrong certificates (or no certificates) to be used.

---
Repository: /testbed
