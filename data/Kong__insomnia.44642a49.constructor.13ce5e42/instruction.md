# Bug Report

### Describe the bug
When creating a Certificate object, the `disabled` property is not being set correctly. Instead of using the `disabled` value from the options, it appears to be getting set to the `passphrase` value.

### Reproduction
```js
const cert = new Certificate({
  name: 'test-cert',
  matches: ['https://example.com/*'],
  key: { src: './key.pem' },
  cert: { src: './cert.pem' },
  passphrase: 'secret123',
  disabled: false
});

console.log(cert.disabled); // Expected: false, but getting 'secret123'
```

### Expected behavior
The `disabled` property should be set to the value provided in `options.disabled`, not `options.passphrase`. A certificate should be able to be enabled/disabled independently of whether it has a passphrase.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
