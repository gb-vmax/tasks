# Bug Report

### Describe the bug

I'm experiencing an issue where named function expressions are not being included correctly in the bundle. When a function has a name (not just assigned to a variable), the function name identifier seems to be getting lost or not properly included in the output.

### Reproduction

```js
const myFunc = function namedFunction() {
  console.log(namedFunction.name);
};

myFunc();
```

When this code is bundled, the function name `namedFunction` is not available inside the function body, causing unexpected behavior or errors.

### Expected behavior

The function name identifier should be accessible within the function body for named function expressions. The bundled output should preserve the function name so that recursive calls or references to the function name work correctly.

### Additional context

This seems to affect named function expressions specifically. Anonymous functions and regular function declarations appear to work fine. The issue might be related to how function identifiers are being processed during the inclusion phase.

---
Repository: /testbed
