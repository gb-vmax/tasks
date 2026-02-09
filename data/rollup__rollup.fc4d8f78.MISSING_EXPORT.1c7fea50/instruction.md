# Bug Report

### Describe the bug

When Rollup detects missing exports, the warning message displays incorrect information. The exporter and binding names appear to be swapped in the error output, and the first warning in the list is being skipped entirely.

### Reproduction

Create a project with missing exports:

```js
// module.js
export const foo = 'bar';

// main.js
import { foo, missingExport } from './module.js';
```

When bundling this with Rollup, the missing export warning shows:
```
module.js is not exported by missingExport
```

But it should show:
```
missingExport is not exported by module.js
```

Also, if there are multiple missing exports, only warnings after the first one are displayed.

### Expected behavior

The warning should correctly identify which binding is missing from which module, with the format:
```
[binding] is not exported by [exporter]
```

All missing export warnings should be displayed, not just those after the first one.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
