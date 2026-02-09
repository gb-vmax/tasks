# Bug Report

### Describe the bug
When creating a Certificate object with the `disabled` property set to `true`, the certificate appears to be enabled instead of disabled. The boolean value seems to be inverted from what's expected.

### Reproduction
```js
const cert = new Certificate({
  name: 'test-cert',
  matches: ['https://example.com/*'],
  key: { src: '/path/to/key' },
  cert: { src: '/path/to/cert' },
  disabled: true
});

// Expected: cert.disabled should be true
// Actual: cert.disabled is false
console.log(cert.disabled); // prints: false
```

Similarly, when setting `disabled: false`:
```js
const cert = new Certificate({
  name: 'test-cert',
  matches: ['https://example.com/*'],
  key: { src: '/path/to/key' },
  cert: { src: '/path/to/cert' },
  disabled: false
});

console.log(cert.disabled); // prints: true (should be false)
```

### Expected behavior
The `disabled` property should reflect the value passed in the constructor options. If I pass `disabled: true`, the certificate should be disabled. If I pass `disabled: false`, it should be enabled.

### System Info
- Package: insomnia-sdk
- Version: latest

---
Repository: /testbed
