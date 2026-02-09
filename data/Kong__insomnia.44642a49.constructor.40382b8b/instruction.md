# Bug Report

### Describe the bug

When creating a Certificate object with incomplete PEM format configuration (only `key` or only `cert` specified), the certificate is being automatically disabled instead of using the `disabled` property from the options. This breaks existing behavior where certificates could be created with partial configuration and the `disabled` flag would be respected.

### Reproduction

```js
const certificate = new Certificate({
  name: 'My Certificate',
  matches: ['https://example.com/*'],
  key: { src: '/path/to/key.pem' },
  disabled: false  // This is being ignored
});

console.log(certificate.disabled);  // Expected: false, Actual: true
```

Also happens when only cert is provided:

```js
const certificate = new Certificate({
  name: 'My Certificate',
  matches: ['https://example.com/*'],
  cert: { src: '/path/to/cert.pem' },
  disabled: false
});

console.log(certificate.disabled);  // Expected: false, Actual: true
```

### Expected behavior

The certificate should respect the `disabled` property passed in the options, regardless of whether the certificate configuration is complete or not. Validation logic should not automatically override user-specified settings.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
