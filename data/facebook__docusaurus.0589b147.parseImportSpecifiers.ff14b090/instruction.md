# Bug Report

### Describe the bug

I'm encountering an issue with import statement parsing in MDX files. When trying to use mixed import syntax (default import combined with named imports), the parser seems to fail or produce unexpected results.

### Reproduction

```jsx
import React, { useState, useEffect } from 'react'
import Component, { namedExport } from './component'
```

When I try to use this common import pattern in my MDX files, the parsing doesn't work as expected. The imports that combine a default import with named imports (separated by comma) are not being handled correctly.

### Expected behavior

The parser should correctly handle mixed import statements where a default import is followed by named imports, just like standard JavaScript/JSX files do. This is a very common pattern in React applications.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This used to work fine in previous versions. Not sure what changed but it's blocking my ability to use standard React import patterns in MDX.

---
Repository: /testbed
