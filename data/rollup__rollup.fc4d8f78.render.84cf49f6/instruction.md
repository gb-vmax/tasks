# Bug Report

### Describe the bug

When using JSX with renamed identifiers, the output code is incorrect. Variables that should be renamed are not being updated in the generated code, while native elements are being processed multiple times incorrectly.

### Reproduction

```jsx
import { Component } from 'react';

// When Component is renamed during bundling
<Component />
```

The identifier `Component` should be renamed in the output if the variable is renamed (e.g., due to minification or name conflicts), but it stays as the original name instead.

### Expected behavior

When a JSX identifier references a variable that gets renamed during the build process, the JSX usage should also be updated to use the new name. The renaming logic should work correctly so that:
1. If a variable is renamed, the JSX identifier should reflect that change
2. Native elements should only be processed once, not multiple times

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
