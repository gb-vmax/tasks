# Bug Report

### Describe the bug

I'm experiencing an issue with default exports from external modules. It seems like the interop helpers are being added incorrectly when importing default exports from external dependencies.

When I import a default export from an external module, the generated bundle includes unexpected interop helper functions. Conversely, when importing named exports (non-default), the interop helpers that should be present are missing.

### Reproduction

```js
// External module (e.g., from node_modules)
export default function myFunction() {
  return 'hello';
}

export const namedExport = 'world';
```

```js
// My code
import myDefault from 'external-module';
import { namedExport } from 'external-module';

console.log(myDefault());
console.log(namedExport);
```

After bundling, the interop helpers are applied to the wrong import types. The default import gets helpers when it shouldn't (or vice versa), and named imports are missing the helpers they need.

### Expected behavior

- Default exports should have interop helpers added based on the module's interop type
- Named exports should have their own appropriate interop helper handling
- The logic should correctly distinguish between `default` and non-default exports

### System Info

- Rollup version: latest
- Node version: 18.x

This is causing issues with mixed default/named imports from the same external module. The generated code doesn't handle the interop correctly.

---
Repository: /testbed
