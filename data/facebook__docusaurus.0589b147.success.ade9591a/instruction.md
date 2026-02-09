# Bug Report

### Describe the bug

The `logger.success()` function is not properly handling interpolated values. When passing template strings with multiple values, the output is missing the first interpolated value.

### Reproduction

```js
import logger from '@docusaurus/logger';

// This should output: "[SUCCESS] User alice has 5 points"
// But it outputs: "[SUCCESS] User has 5 points" (missing 'alice')
logger.success`User ${'alice'} has ${5} points`;
```

### Expected behavior

All interpolated values should be included in the success message output. The logger should properly format template strings with all provided values.

### Additional context

This seems to affect only the `success()` method. Other logger methods like `info()` and `warn()` appear to work correctly with template string interpolation.

---
Repository: /testbed
