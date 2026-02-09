# Bug Report

### Describe the bug

I'm encountering an issue with function call arguments not being rendered correctly in the output. When a function has multiple arguments and some of them are excluded during tree-shaking, the last included argument is missing from the generated code.

### Reproduction

```js
// Input code
function test(a, b, c) {
  console.log(a, b, c);
}

// When argument 'c' is excluded but 'a' and 'b' should be included
test(1, 2, 3);

// Expected output: test(1, 2)
// Actual output: test(1)
```

The problem occurs when there are trailing arguments that get excluded - the rendering logic seems to skip the last included argument instead of including it.

### Expected behavior

All included arguments up to and including the last one should be rendered in the output. If we have three arguments where the third is excluded, both the first and second arguments should appear in the final code.

### Additional context

This appears to affect any function or constructor calls where:
1. There are multiple arguments
2. One or more trailing arguments are excluded
3. At least two arguments before the excluded ones should be included

The bundled output is missing arguments that should be present, which breaks the functionality of the code.

---
Repository: /testbed
