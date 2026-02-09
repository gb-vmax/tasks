# Bug Report

### Describe the bug

I'm experiencing an issue with namespace imports where accessing deeply nested properties from imported namespaces causes infinite recursion or hangs the bundler. This seems to happen specifically when trying to access properties that are multiple levels deep in a namespace object.

### Reproduction

```js
// lib.js
export const utils = {
  helpers: {
    formatDate: () => {}
  }
};

// main.js
import * as lib from './lib.js';

// This causes the bundler to hang/crash
const formatter = lib.utils.helpers.formatDate;
```

### Expected behavior

Should be able to access nested properties from namespace imports without the bundler hanging. The property access should resolve correctly and the build should complete successfully.

### Additional context

This started happening recently and I suspect it might be related to how namespace variables are being resolved. Simple namespace imports (one level deep) seem to work fine, but anything with multiple levels of nesting triggers the issue.

---
Repository: /testbed
