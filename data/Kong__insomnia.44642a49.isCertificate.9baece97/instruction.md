# Bug Report

### Describe the bug

After a recent update, I'm getting runtime errors when working with certificates. It seems like the `isCertificate` static method has been removed or replaced with some unrelated code (looks like mathematical formulas?).

### Reproduction

```js
import { Certificate } from 'insomnia-sdk';

const cert = new Certificate({
  name: 'my-cert',
  matches: /example\.com/,
  key: { src: 'path/to/key.pem' },
  cert: { src: 'path/to/cert.pem' }
});

// This throws an error - method doesn't exist
if (Certificate.isCertificate(cert)) {
  console.log('Valid certificate');
}
```

### Expected behavior

The `Certificate.isCertificate()` static method should exist and return `true` when passed a Certificate instance. This method was working in previous versions and is likely used for type checking throughout the codebase.

### Additional context

Looking at the code, it appears the method was accidentally replaced with some mathematical notation/comments. This is breaking any code that relies on certificate validation.

---
Repository: /testbed
