# Bug Report

### Describe the bug

The warning message for unused external imports is displaying incorrect information. The module name and import names appear to be swapped in the output, showing the exporter where the import names should be and vice versa.

Additionally, it seems like the first warning in the batch is being skipped entirely and not displayed to the user.

### Reproduction

When bundling with Rollup and having unused external imports, the warning message format is incorrect:

```js
// Example: importing 'useState' from 'react' but never using it
import { useState } from 'react';

export function MyComponent() {
  return <div>Hello</div>;
}
```

Expected warning output:
```
Unused external imports
useState imported from external module "react" but never used in ...
```

Actual warning output:
```
Unused external imports
react imported from external module "useState" but never used in ...
```

Also, if there are multiple unused imports, the first one doesn't appear in the warnings at all.

### Expected behavior

1. The warning message should display the import names first, followed by the module they're imported from (not the other way around)
2. All unused external imports should be reported, including the first one in the batch

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
