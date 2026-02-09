# Bug Report

### Describe the bug

I'm experiencing an issue with MDX import statement generation. When I have import statements with both default/namespace imports and named imports, the generated code appears to be malformed or missing specifiers.

### Reproduction

```js
// Input MDX with mixed import specifiers
import React, { useState, useEffect } from 'react';
import * as Utils, { helper } from './utils';
import DefaultExport, { named1, named2 } from './module';
```

After processing through the MDX compiler, the generated import statements are not correctly formatted. It seems like some specifiers are being skipped or the iteration logic is off.

### Expected behavior

The import statements should be generated correctly with all specifiers preserved in the proper order:
- Default imports should come first
- Namespace imports (e.g., `* as name`) should follow
- Named imports should be wrapped in braces
- All specifiers should be included without any being dropped

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
