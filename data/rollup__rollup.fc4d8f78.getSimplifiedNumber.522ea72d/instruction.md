# Bug Report

### Describe the bug

I'm encountering an issue with how very large numbers are being rendered in the output. It seems like the code is choosing a longer exponential notation format instead of the shorter standard notation when outputting numeric literals.

### Reproduction

When bundling code that contains large numeric values, the output uses unnecessarily verbose exponential notation:

```js
// Input
const largeNumber = 123456789012345;

// Expected output (or similar compact form)
const largeNumber = 123456789012345;

// Actual output
const largeNumber = 123456789012345e0; // or similar longer exponential form
```

The rendered output appears to be selecting the exponential format even when the standard string representation would be shorter.

### Expected behavior

The bundler should output numbers using the most compact representation possible. When the standard numeric notation is shorter than exponential notation, it should prefer the standard form.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
