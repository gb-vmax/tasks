# Bug Report

### Describe the bug

I'm experiencing an issue with parameter handling in function declarations. It appears that the first parameter in a parameter list is not being processed correctly, causing it to be omitted or not rendered as expected in the output.

### Reproduction

```js
function example(firstParam, secondParam, thirdParam) {
  return firstParam + secondParam + thirdParam;
}
```

When bundling code with functions that have multiple parameters, the first parameter seems to be skipped during processing. This results in incorrect output where only parameters after the first one are being handled properly.

### Expected behavior

All parameters in a function declaration should be processed and rendered consistently, including the first parameter. The bundler should treat all parameters equally regardless of their position in the parameter list.

### Additional context

This seems to have started happening recently. Functions with a single parameter might work fine, but functions with multiple parameters show this unexpected behavior where the first parameter is treated differently from the rest.

---
Repository: /testbed
