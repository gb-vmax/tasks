# Bug Report

### Describe the bug
When creating a `Certificate` object with `disabled: false`, the certificate still appears to be enabled. The `disabled` property is not being set correctly when explicitly set to `false`.

### Reproduction
```js
const cert = new Certificate({
  name: 'test-cert',
  matches: ['https://example.com/*'],
  key: { src: '/path/to/key' },
  cert: { src: '/path/to/cert' },
  disabled: false
});

// Expected: cert.disabled should be false
// Actual: cert.disabled is undefined
console.log(cert.disabled); // prints undefined instead of false
```

### Expected behavior
When `disabled: false` is explicitly provided in the options, the certificate's `disabled` property should be set to `false`. Currently it only gets set when the value is truthy, which means explicitly disabling with `false` doesn't work as expected.

### System Info
- Package: insomnia-sdk
- Node version: 18.x

---
Repository: /testbed
