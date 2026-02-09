# Bug Report

### Describe the bug

The `isCertificate` method is not working as expected after a recent update. It seems like the function signature changed and now requires an additional parameter, but the behavior is inconsistent with how it was working before.

### Reproduction

```js
const cert = {
  _kind: 'Certificate',
  name: 'my-cert',
  key: { src: '/path/to/key' }
};

// This used to work but now returns unexpected results
Certificate.isCertificate(cert);
```

When I pass a certificate object that was previously valid, the method doesn't recognize it properly anymore. I noticed this started happening after updating to the latest version.

### Expected behavior

The `isCertificate` method should correctly identify valid certificate objects without requiring any additional configuration or parameters. Previously working code should continue to work without modifications.

### Additional context

This is breaking existing code that relies on certificate validation. The method seems to have changed its validation logic, but I'm not sure what the new requirements are or if this is a regression.

---
Repository: /testbed
