# Bug Report

### Describe the bug
The `Certificate.isCertificate()` method is not working as expected. After a recent update, it seems like the method signature has changed and now requires a second parameter, but this breaks existing code that was using the method with just one argument.

### Reproduction
```js
const cert = new Certificate({
  name: 'test-cert',
  key: { src: '/path/to/key' },
  cert: { src: '/path/to/cert' }
});

// This used to work but now behaves differently
const isValid = Certificate.isCertificate(cert);
```

When checking if an object is a certificate, the method now seems to have different behavior depending on some mode parameter that wasn't there before. The default behavior should just check if something is a Certificate instance, but it's unclear what the expected usage is now.

### Expected behavior
`Certificate.isCertificate()` should work with a single argument like it did before and correctly identify Certificate objects without requiring additional parameters.

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
