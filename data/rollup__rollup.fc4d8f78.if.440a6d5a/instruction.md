# Bug Report

### Describe the bug

When bundling a module with named exports, the exports are not being included in the output bundle unless `includeNamespaceMembers` is explicitly set to true. This causes runtime errors when trying to import specific named exports from the bundle.

### Reproduction

```js
// entry.js
export const foo = 'bar';
export const baz = 42;

// After bundling and trying to import:
import { foo } from './bundle.js';
// Error: foo is not defined
```

The issue appears when:
1. Creating a module with named exports
2. Bundling without namespace member inclusion
3. The named exports are missing from the final bundle even though they should be included

### Expected behavior

Named exports should be included in the bundle by default, regardless of the `includeNamespaceMembers` setting. The condition should be checking if we should include namespace members OR if it's a regular export (not the synthetic named export).

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
