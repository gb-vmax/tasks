# Bug Report

### Describe the bug
Certificate configuration is not working properly - the key and cert files appear to be swapped, and certificate matching patterns are not being applied correctly when they should be.

### Reproduction
```js
const cert = new Certificate({
  name: 'my-cert',
  matches: ['https://example.com/*'],
  key: { src: '/path/to/private.key' },
  cert: { src: '/path/to/certificate.crt' },
  disabled: false
});

// The key and cert are swapped
console.log(cert.key); // Shows certificate.crt instead of private.key
console.log(cert.cert); // Shows private.key instead of certificate.crt

// Also, matches array is empty even though disabled is false
console.log(cert.matches); // Empty array when it should contain the pattern
```

### Expected behavior
- The `key` property should contain the private key file reference
- The `cert` property should contain the certificate file reference  
- The `matches` patterns should be populated when `disabled` is `false`

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

This is breaking SSL/TLS client certificate authentication for my API requests. The certificates are being loaded with incorrect file mappings.

---
Repository: /testbed
