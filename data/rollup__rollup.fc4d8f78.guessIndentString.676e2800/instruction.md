# Bug Report

### Describe the bug

When bundling code that uses 2-space indentation, the indent detection is not working correctly. The bundler seems to be defaulting to tabs instead of preserving the 2-space indentation style.

### Reproduction

```js
const code = `
function test() {
  if (true) {
    return 42;
  }
}
`;

// Bundle this code
// Expected: Output preserves 2-space indentation
// Actual: Output uses tabs instead
```

### Expected behavior

When the source code uses 2-space indentation, the bundler should detect this and preserve it in the output. The indent detection logic should recognize 2-space indentation as a valid spacing pattern.

### Additional context

This seems to affect code that consistently uses 2 spaces for indentation. The bundler appears to be falling back to tabs even when the input clearly uses spaces. This breaks formatting consistency in projects that enforce 2-space indentation via linters/formatters.

---
Repository: /testbed
