# Bug Report

### Describe the bug

I'm experiencing an issue with logical expressions in my code where the bundler seems to be getting stuck in an infinite loop or taking an extremely long time to process certain logical operators. This appears to be related to how branch resolution is being analyzed.

### Reproduction

```js
// This code causes the bundler to hang
function test() {
  const result = condition1 || condition2;
  return result;
}

// Also happens with && operators
function test2() {
  const result = condition1 && condition2;
  return result;
}
```

When I try to bundle code containing logical expressions (OR/AND operators), the build process never completes. It seems to get stuck during the analysis phase and I have to manually kill the process.

### Expected behavior

The bundler should complete the build process in a reasonable amount of time without hanging.

### Additional context

This started happening recently and I'm not sure what changed. The same code used to bundle fine before. CPU usage spikes to 100% when this happens, suggesting some kind of infinite loop in the bundler's internal logic.

---
Repository: /testbed
