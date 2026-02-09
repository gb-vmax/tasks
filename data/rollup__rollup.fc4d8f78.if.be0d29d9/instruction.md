# Bug Report

### Describe the bug

When bundling code that uses helper functions, some helpers that should be included in the output are missing. This causes runtime errors because the code tries to reference helper functions that don't exist in the generated bundle.

### Reproduction

```js
// Input code that requires certain helpers
const result = someGlobalHelper();

// After bundling, the helper is not included in the output
// even though it's being accessed in the code
```

The generated output is missing the necessary helper definitions, leading to `ReferenceError: someGlobalHelper is not defined` at runtime.

### Expected behavior

All helper functions that are accessed in the code should be included in the generated bundle. If a global helper is referenced anywhere in the code, it should be present in the helpers block of the output.

### Additional context

This appears to be related to how the helpers block is constructed. The bundle successfully detects which globals are accessed, but they're not being added to the final output correctly.

---
Repository: /testbed
