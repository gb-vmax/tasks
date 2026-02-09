# Bug Report

### Describe the bug

I'm encountering an issue with parsing import statements in MDX files. When I have an import statement with a default import followed by named imports, the parser seems to be handling it incorrectly.

### Reproduction

```jsx
import React, { useState, useEffect } from 'react';
```

When using an import statement like the one above (default import + named imports), the parsing behavior is unexpected. The default import appears to be processed, but then the parser stops and doesn't continue to parse the named imports that follow.

### Expected behavior

The parser should correctly handle import statements that combine both default and named imports. Both `React` and `{ useState, useEffect }` should be parsed as separate import specifiers.

### Additional context

This seems to affect any MDX file that uses this common import pattern. Files with only default imports OR only named imports work fine, but combining them causes issues.

---
Repository: /testbed
