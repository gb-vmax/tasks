# Bug Report

### Describe the bug

I'm experiencing an issue with parsing import statements that have both default and named imports. When I try to use an import statement with a default import followed by named imports, the parser seems to be incorrectly handling the comma separator.

### Reproduction

```js
import React, { useState, useEffect } from 'react';
```

When parsing MDX files with this kind of import syntax, the named imports after the default import are not being recognized properly. It seems like the parser is returning early when it encounters the comma after the default import specifier.

### Expected behavior

The parser should correctly handle import statements that include both:
1. A default import (e.g., `React`)
2. Named imports (e.g., `{ useState, useEffect }`)

Both parts should be parsed and included in the result.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This is blocking our ability to use standard React import patterns in MDX files. Any help would be appreciated!

---
Repository: /testbed
