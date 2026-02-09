# Bug Report

### Describe the bug

When building with external imports that are unused, the warning message for `UNUSED_EXTERNAL_IMPORT` is not displaying the first warning in the list. It seems like warnings are being skipped and not all unused external imports are being reported to the user.

### Reproduction

1. Create a project with external dependencies
2. Import something from an external module but don't use it in multiple files
3. Run the build
4. Observe that the first unused external import warning is missing from the output

Example setup:
```js
// file1.js
import { unused1 } from 'external-package';

// file2.js  
import { unused2 } from 'external-package';

// file3.js
import { unused3 } from 'external-package';
```

### Expected behavior

All unused external imports should be reported in the warning output. Currently it appears that only warnings starting from index 1 are being shown, which means the first warning is always omitted.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
