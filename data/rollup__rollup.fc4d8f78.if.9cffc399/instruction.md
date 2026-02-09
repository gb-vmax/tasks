# Bug Report

### Describe the bug

I'm experiencing an issue with default exports when bundling external modules. It seems like the interop helpers for default exports are being applied to the wrong chunks.

When I import a default export from an external module, the generated bundle includes unnecessary interop helpers. Conversely, when importing named exports (non-namespace), the default interop helpers that should NOT be added are actually being added to the chunk dependencies.

### Reproduction

```js
// external-module.js (external dependency)
export default function myFunction() {
  return 'hello';
}

export const namedExport = 'world';

// main.js
import myDefault from 'external-module';
import { namedExport } from 'external-module';

console.log(myDefault());
console.log(namedExport);
```

When bundling this, the interop helpers are applied incorrectly - named exports get default interop helpers added when they shouldn't, and default exports don't get the helpers they need.

### Expected behavior

- Default exports should have default interop helpers applied when needed
- Named (non-namespace) exports should NOT have default interop helpers applied
- The `deconflictedDefault` set should only contain chunks for actual default exports

### System Info

- Rollup version: latest
- Node version: 18.x

This seems like it might be a regression from a recent change. The logic for checking `variable.name === 'default'` appears to be inverted somehow.

---
Repository: /testbed
