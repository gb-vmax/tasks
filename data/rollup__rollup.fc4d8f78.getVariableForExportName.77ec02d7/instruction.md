# Bug Report

### Describe the bug

When importing from external modules, the `importersByExportedName` map is not being populated correctly for newly created external variables. This causes issues with tracking which modules are importing specific exports.

### Reproduction

```js
// External module exports a variable that hasn't been cached yet
import { someNewExport } from 'external-package';

// The importersByExportedName should track this import relationship
// but it's not being registered for new exports
```

The problem occurs when:
1. An export name is requested that doesn't exist in the declarations cache
2. A new ExternalVariable is created for this export
3. The import chain information is not recorded in `importersByExportedName`

This means that for any export that gets lazily created, we lose track of which modules are importing it, while exports that were already declared work fine.

### Expected behavior

All exports from external modules should have their import relationships tracked in `importersByExportedName`, regardless of whether the variable was previously cached or newly created.

---
Repository: /testbed
