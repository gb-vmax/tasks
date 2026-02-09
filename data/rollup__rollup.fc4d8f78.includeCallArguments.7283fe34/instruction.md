# Bug Report

### Describe the bug

I'm experiencing an issue with tree-shaking where imported functions are being incorrectly removed from the bundle even though they're actually being used. This seems to happen specifically when the imported module is assigned to a const variable and then methods are called on that variable.

### Reproduction

```js
import('./module.js').then(mod => {
  const myModule = mod;
  myModule.someFunction(); // This call gets tree-shaken out incorrectly
});
```

Or with async/await:

```js
const myModule = await import('./module.js');
myModule.someFunction(); // Function call is not included in bundle
```

### Expected behavior

When calling methods on a const variable that holds an imported module, those methods should be included in the final bundle. The tree-shaking should recognize that these are legitimate function calls that need to be preserved.

### Additional context

This appears to be related to how member expressions on imported modules are being analyzed. The issue only occurs when the import is assigned to a variable first - direct calls like `(await import('./module.js')).someFunction()` seem to work fine.

---
Repository: /testbed
