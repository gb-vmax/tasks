# Bug Report

### Describe the bug

I'm experiencing an issue with function parameters not being rendered correctly in the output. It seems like some parameters are being dropped or not included when they should be.

### Reproduction

```js
function example(a, b, c) {
  return a + b + c;
}
```

When this gets processed, the first parameter appears to be handled differently than the rest. The subsequent parameters (b, c) seem to have inconsistent rendering behavior - sometimes they show up in the output, sometimes they don't.

### Expected behavior

All function parameters should be consistently rendered in the output, regardless of their position in the parameter list. The first parameter and all following parameters should be treated the same way.

### Additional context

This appears to affect functions with multiple parameters. Single-parameter functions seem to work fine, but once you have 2 or more parameters, the behavior becomes unpredictable for parameters after the first one.

---
Repository: /testbed
