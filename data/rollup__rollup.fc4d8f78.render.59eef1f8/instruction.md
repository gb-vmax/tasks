# Bug Report

### Describe the bug

Tagged template expressions are being rendered in the wrong order, causing the template literal to appear before the tag function in the generated output.

### Reproduction

```js
// Input code
const result = myTag`Hello ${name}!`;

// Expected output
myTag`Hello ${name}!`

// Actual output
`Hello ${name}!`myTag
```

When using tagged template expressions, the tag function and template literal are being output in reverse order during code generation. This produces invalid JavaScript syntax.

### Steps to reproduce

1. Create a tagged template expression with any tag function
2. Bundle/compile the code
3. The output will have the template literal rendered before the tag function

### Expected behavior

The tag function should be rendered first, followed by the template literal, maintaining the correct syntax for tagged template expressions.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
