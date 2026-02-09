# Bug Report

### Describe the bug

I'm experiencing an issue with external module imports where the module declarations map is not being properly updated. When importing from an external module, the variable is created but not stored in the declarations map, which causes problems on subsequent imports of the same export.

### Reproduction

```js
// External module with named export
// external-lib.js
export const myExport = 'value';

// First import works fine
import { myExport } from 'external-lib';

// Subsequent imports or re-exports of the same name
// behave unexpectedly - seems like declarations aren't being tracked
export { myExport } from 'external-lib';
```

### Expected behavior

When getting a variable for an export name from an external module, the declaration should be stored in the declarations map so that future lookups for the same export name return the same variable instance. Each export should only create one ExternalVariable instance that gets reused.

### Additional context

This seems to affect how external module exports are tracked and could lead to duplicate variable instances being created for the same export name.

---
Repository: /testbed
