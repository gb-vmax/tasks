# Bug Report

### Describe the bug

When using `import.meta.ROLLUP_FILE_URL_*` properties, the file URL resolution is not working correctly. The code seems to be checking for the wrong prefix when determining if the property should be treated as a URL object.

### Reproduction

```js
// In your module code
const fileUrl = import.meta.ROLLUP_FILE_URL_12345;

// Expected: Should resolve to a URL object
// Actual: Resolves incorrectly due to prefix mismatch
```

The issue appears when accessing dynamically resolved file URLs through `import.meta`. The prefix detection logic seems to have gotten out of sync, causing the wrong type of URL to be generated.

### Expected behavior

When accessing `import.meta.ROLLUP_FILE_URL_*` properties, they should be correctly identified and resolved as URL objects. The prefix checking should properly distinguish between file URL objects and regular file paths.

### Additional context

This affects how imported assets are resolved in the bundled output. The URL object detection is critical for proper asset handling in different module formats.

---
Repository: /testbed
