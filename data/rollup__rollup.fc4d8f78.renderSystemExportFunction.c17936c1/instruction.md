# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS output format where exported variables from arrow function expressions are not being properly captured. The exports object seems to be missing from the IIFE wrapper, causing the exported values to not be available in the SystemJS module.

### Reproduction

```js
// Input code
export default () => someValue;

// Expected SystemJS output should include exports parameter
// But the generated code is missing proper export handling
```

When bundling code that exports arrow functions or other expressions, the SystemJS format output doesn't correctly wrap the expression with the necessary export mechanism. The exported value is not accessible from other modules trying to import it.

### Expected behavior

The SystemJS format should properly wrap exported expressions in an IIFE that includes both the value parameter and the exports object, ensuring that the exported value is correctly registered with the SystemJS module loader.

### System Info
- Rollup version: latest
- Output format: systemjs
- Node version: 18.x

---
Repository: /testbed
