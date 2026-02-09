# Bug Report

### Describe the bug

I'm encountering an issue with how very small numbers are being rendered in the output. It seems like negative exponents in scientific notation are being calculated incorrectly, resulting in wrong values.

### Reproduction

When I have code that generates very small decimal numbers, the output is completely wrong. For example:

```js
// Input: 0.00001
// Expected output: 1e-5 or 0.00001
// Actual output: 1e5 (which is 100000!)
```

The same issue appears to affect how negative numbers are handled - the minus sign seems to be getting stripped out in some cases.

### Expected behavior

Small numbers should be correctly represented either in their decimal form or in proper scientific notation with the correct exponent sign and value. Negative numbers should maintain their sign.

### Additional context

This appears to affect the literal value rendering, particularly when the code is trying to choose between exponential and string representations of numbers. The exponential notation for small decimals is coming out with the wrong exponent value, making tiny numbers appear as very large ones.

---
Repository: /testbed
