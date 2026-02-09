# Bug Report

### Describe the bug

Arrow function parameters with destructuring patterns are not being included in the bundle output. When using destructured parameters in arrow functions, the parameter declarations are missing from the generated code, causing runtime errors.

### Reproduction

```js
// Input code
const fn = ({ a, b }) => {
  console.log(a, b);
};

export { fn };
```

After bundling, the destructured parameters `{ a, b }` are not properly included in the output, resulting in broken code.

This seems to affect arrow functions specifically when they have non-identifier parameters (like object/array destructuring patterns).

### Expected behavior

Arrow function parameters with destructuring should be included in the bundle output just like regular identifier parameters. The generated code should maintain the full parameter signature.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
