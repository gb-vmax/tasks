# Bug Report

### Describe the bug

The `throwError` function in the logger is producing error messages incorrectly. When calling `throwError` with template strings and interpolation values, the error message ends up being the raw template string instead of the interpolated result.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should throw an error with message "Failed to load file: config.json"
// But instead throws with message "Failed to load file: %s"
try {
  logger.throwError`Failed to load file: ${'config.json'}`;
} catch (error) {
  console.log(error.message); // Outputs wrong message
}
```

### Expected behavior

When using template literal syntax with `throwError`, the error message should contain the interpolated values, not the raw template string.

For example:
- Input: `throwError\`Failed to load file: ${'config.json'}\``
- Expected error message: `"Failed to load file: config.json"`
- Actual error message: `"Failed to load file: %s"` (or similar placeholder)

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
