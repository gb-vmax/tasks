# Bug Report

### Describe the bug

I'm encountering an issue with import statement parsing in MDX files. When using a default import followed by named imports (separated by a comma), the parser seems to be handling the comma incorrectly and returning early instead of continuing to parse the named imports.

### Reproduction

```js
// This import statement doesn't parse correctly
import React, { useState, useEffect } from 'react'

// The parser appears to return after seeing the comma following the default import
// and doesn't process the named imports in the curly braces
```

### Expected behavior

The parser should correctly handle import statements that include both a default import and named imports. After parsing the default import and encountering a comma, it should continue to parse any named imports that follow.

Example of what should work:
```js
import DefaultExport, { namedExport1, namedExport2 } from 'module'
```

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems like a regression in the import parsing logic. The parser is exiting too early when it encounters the comma after a default import specifier.

---
Repository: /testbed
