# Bug Report

### Describe the bug

Warnings that should be deferred until the end of the build are now being printed immediately. This makes the CLI output confusing because warnings that are supposed to be grouped and summarized at the end are now appearing inline during the build process.

### Reproduction

```js
// When building with warnings that have codes handled by deferredHandlers
// (e.g., CIRCULAR_DEPENDENCY, UNUSED_EXTERNAL_IMPORT, etc.)
// These warnings are now printed immediately instead of being batched

import { rollup } from 'rollup';

const bundle = await rollup({
  input: 'src/index.js',
  // ... config that triggers deferred warnings
});

// Expected: Warnings collected and shown at end
// Actual: Warnings shown immediately during build
```

### Expected behavior

Warnings with codes that have deferred handlers should be collected and displayed together at the end of the build process, not shown immediately as they occur. This allows for better grouping and summarization of similar warnings.

### Additional context

This seems to have changed recently. The deferred warning system was working correctly before, where warnings would be batched and shown with a summary count at the end.

---
Repository: /testbed
