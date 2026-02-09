# Bug Report

### Describe the bug

I'm experiencing an issue where named function expressions used in IIFEs (Immediately Invoked Function Expressions) are being incorrectly tree-shaken/removed during the build process. The function name seems to disappear even though it's being used within the function body itself.

### Reproduction

```js
const result = (function myFunc() {
  // Reference to myFunc inside the function body
  return typeof myFunc === 'function' ? 'works' : 'broken';
})();

console.log(result); // Expected: 'works', Actual: 'broken'
```

Another case:
```js
(function factorial(n) {
  if (n <= 1) return 1;
  return n * factorial(n - 1); // Recursive call fails
})(5);
```

The function name identifier is being removed even when it's referenced within the function scope. This breaks recursive named function expressions and any code that relies on the function name being available inside the function body.

### Expected behavior

Named function expressions should retain their name identifier when used in an IIFE pattern, especially when the name is referenced within the function body itself. The bundler should recognize that the function name is in use and not remove it.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
