# Bug Report

### Describe the bug

I'm experiencing an issue with SystemJS export rendering where the generated code has incorrect variable names in the IIFE wrapper. When using `export default` with an expression, the output code references a variable `v` that doesn't exist in the function parameters.

### Reproduction

When bundling code with a default export expression like:

```js
export default someExpression;
```

The generated SystemJS output creates an IIFE with mismatched parameter names. The function is defined with parameter `exports` but the body tries to use `v`, causing a ReferenceError at runtime.

Expected generated code structure:
```js
(function(exports) { 
  // ... export statement ..., v 
})(actualValue)
```

But the parameter name and usage don't align, breaking the export functionality.

### Expected behavior

The IIFE wrapper should use consistent variable naming - the parameter name should match what's referenced in the function body. The exported value should be properly captured and returned.

### System Info
- Rollup version: latest
- Output format: SystemJS
- Node version: 18.x

This seems to have broken default exports when using the SystemJS format. Any expression-based default export now fails at runtime.

---
Repository: /testbed
