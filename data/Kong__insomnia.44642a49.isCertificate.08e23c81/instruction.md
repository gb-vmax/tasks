# Bug Report

### Describe the bug

The `Certificate.isCertificate()` method is rejecting valid certificate objects that contain extra properties beyond the core certificate fields. This is causing issues when working with certificate objects that have been extended or augmented with additional metadata.

### Reproduction

```js
const cert = {
  _kind: 'Certificate',
  name: 'My Certificate',
  cert: { src: '/path/to/cert.pem' },
  key: { src: '/path/to/key.pem' },
  customField: 'some metadata'  // Extra property
};

// This now returns false even though it's a valid certificate
Certificate.isCertificate(cert);  // Expected: true, Actual: false
```

### Expected behavior

`isCertificate()` should return `true` for objects that have the `_kind: 'Certificate'` property and valid certificate structure, even if they contain additional properties. Extra properties shouldn't invalidate a certificate object.

This is particularly problematic when:
- Working with certificates that have been serialized/deserialized with extra metadata
- Extending certificate objects with custom tracking or logging fields
- Integrating with systems that add their own properties to certificate objects

### System Info
- insomnia-sdk version: latest
- Node version: 18.x

---
Repository: /testbed
