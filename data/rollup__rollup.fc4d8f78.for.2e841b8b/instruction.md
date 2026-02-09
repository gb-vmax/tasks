# Bug Report

### Describe the bug

I'm encountering an issue with function parameter handling in the bundler. When a function has multiple parameters, some parameters are unexpectedly being excluded from the output even though they're being used.

### Reproduction

```js
function example(a, b, c) {
  console.log(a, b, c);
}

example(1, 2, 3);
```

After bundling, the first parameter seems to be missing or not rendered correctly in the output. This affects functions with 2 or more parameters.

### Expected behavior

All function parameters that are used should be preserved in the bundled output. Each parameter `a`, `b`, and `c` should be included since they're all referenced in the function body.

### Additional context

This seems to have started recently. Functions with a single parameter work fine, but multi-parameter functions are having issues. The bundled code runs but produces incorrect results because parameters are missing.

---
Repository: /testbed
