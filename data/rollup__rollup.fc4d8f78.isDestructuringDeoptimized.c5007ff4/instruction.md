# Bug Report

### Describe the bug

I'm experiencing an issue with destructuring assignments where the optimization detection seems to be inverted. Variables that should be marked as deoptimized are being treated as optimized, and vice versa. This is causing incorrect behavior in my bundled output.

### Reproduction

```js
// Example code that triggers the issue
const obj = { a: 1, b: 2, c: 3 };
const { a, ...rest } = obj;

// The destructuring should be deoptimized in certain cases
// but the behavior is now reversed
console.log(rest); // Unexpected output
```

When using destructuring patterns with rest elements or in complex scenarios, the bundler seems to be making incorrect optimization decisions. Code that should remain unoptimized is being optimized, leading to incorrect runtime behavior.

### Expected behavior

The bundler should correctly identify when destructuring patterns need to be deoptimized and handle them appropriately. The optimization flag should accurately reflect whether deoptimization is needed.

### System Info
- Rollup version: latest
- Node version: 18.x
- OS: macOS

---
Repository: /testbed
