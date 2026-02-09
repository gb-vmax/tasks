# Bug Report

### Describe the bug

I'm experiencing an issue with import statement generation in MDX files. When I have an import statement with a default import, it seems to be getting skipped or not rendered correctly in the output.

### Reproduction

```js
// Input MDX with import statement
import React from 'react';
import { useState } from 'react';

// The generated output is missing the default import
// Expected: import React, { useState } from 'react';
// Actual: import { useState } from 'react';
```

This also happens with namespace imports:

```js
import DefaultExport, * as Utils from './utils';

// The default import gets dropped
```

### Expected behavior

When processing import declarations with multiple specifiers (default import + named imports, or default + namespace), all specifiers should be included in the generated output. The default import should appear first, followed by named or namespace imports.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
