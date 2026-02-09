# Bug Report

### Describe the bug

The `disabled` property on certificates is behaving incorrectly - it seems to be inverted. When I set a certificate as disabled, it actually becomes enabled, and vice versa.

### Reproduction

```js
const cert = new Certificate({
  name: 'test-cert',
  matches: ['https://example.com/*'],
  disabled: true
});

console.log(cert.disabled); // Expected: true, Actual: false
```

When creating a certificate with `disabled: true`, the certificate is actually enabled. Similarly, setting `disabled: false` results in an enabled certificate (which happens to be correct by accident).

### Expected behavior

The `disabled` property should reflect the value passed in the options:
- `disabled: true` should result in a disabled certificate
- `disabled: false` should result in an enabled certificate
- `disabled: undefined` should result in an enabled certificate (default behavior)

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
