# Bug Report

### Describe the bug

I'm experiencing an issue with arrow function parameter handling in Rollup. When using arrow functions with multiple parameters, it appears that the first parameter is being skipped or not processed correctly during bundling.

### Reproduction

```js
// input.js
const myFunc = (a, b, c) => {
  console.log(a, b, c);
};

export { myFunc };
```

When bundling this code, the first parameter `a` seems to not be included properly in the output. This affects tree-shaking and code generation for arrow functions with destructured or complex parameters.

### Expected behavior

All parameters of an arrow function should be processed and included in the bundle, regardless of their position. The first parameter should be treated the same way as subsequent parameters.

### Additional context

This seems to affect arrow functions specifically - regular function declarations appear to work fine. The issue becomes more apparent when using:
- Destructuring in parameters: `(a, {b, c}) => ...`
- Rest parameters: `(first, ...rest) => ...`
- Default values: `(a = 1, b = 2) => ...`

The first parameter in these cases is not being handled correctly during the build process.

---
Repository: /testbed
