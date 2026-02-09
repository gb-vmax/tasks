# Bug Report

### Describe the bug

I'm encountering an issue with import statement parsing where default imports combined with named imports are not being handled correctly. When I have an import statement that includes both a default import and named imports (separated by a comma), the parser seems to be stopping prematurely and not processing the named imports.

### Reproduction

```js
// This import statement is not parsed correctly
import React, { useState, useEffect } from 'react';

// The parser only captures the default import (React)
// and ignores the named imports ({ useState, useEffect })
```

Another example:
```js
import axios, { AxiosError } from 'axios';
// Only 'axios' is recognized, 'AxiosError' is lost
```

### Expected behavior

The parser should correctly handle import statements that contain both default and named imports. All specifiers should be captured and available in the AST.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems to have broken recently as my existing code that relies on these mixed import patterns is no longer working as expected.

---
Repository: /testbed
