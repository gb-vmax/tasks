# Bug Report

### Describe the bug

Arrow function parameters with destructuring patterns are not being included in the output bundle. When using destructured parameters in arrow functions, the destructuring syntax is missing from the generated code, causing runtime errors.

### Reproduction

```js
// Input code
const fn = ({ name, age }) => {
  console.log(name, age);
};

export { fn };
```

After bundling, the destructured parameters are not properly included in the output, leading to issues when the function is called.

### Expected behavior

Arrow functions with destructured parameters should be correctly included in the bundle with their full parameter syntax preserved. The destructuring pattern should appear in the output code.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
