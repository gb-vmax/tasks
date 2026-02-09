# Bug Report

### Describe the bug

I'm encountering an issue with `import.meta.ROLLUP_FILE_URL_*` references not resolving correctly. When using these meta properties in my code, the referenced file names are not being properly extracted, causing the build to fail or produce incorrect output.

### Reproduction

```js
// In my module code
const fileUrl = import.meta.ROLLUP_FILE_URL_referenceId;

// The file reference is not being resolved properly
// Expected: Should resolve to the actual file name
// Actual: Returns null or incorrect file name
```

### Expected behavior

When using `import.meta.ROLLUP_FILE_URL_*` or `import.meta.ROLLUP_FILE_URL_*_OBJ`, the system should correctly:
1. Detect that this is an import meta property reference
2. Extract the reference ID from the property name
3. Return the corresponding file name via the output plugin driver

### Additional context

This seems to affect file URL references specifically. The meta property detection logic might not be handling the `import.meta` case correctly.

---
Repository: /testbed
