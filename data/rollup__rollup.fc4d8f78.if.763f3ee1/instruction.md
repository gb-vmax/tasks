# Bug Report

### Describe the bug

I'm experiencing an issue with export resolution where the module system is incorrectly handling missing export shims. When trying to import a named export that doesn't exist, the behavior seems inverted - it's returning the shim variable when it shouldn't and vice versa.

### Reproduction

```js
// module-a.js
export const foo = 'bar';

// module-b.js
import { foo, nonExistent } from './module-a.js';

console.log(foo); // Should work
console.log(nonExistent); // Should use export shim
```

When importing `nonExistent` which doesn't actually exist in the source module, the export shim variable is not being returned as expected. Instead, it seems like the logic is backwards - the shim is returned for valid exports and not returned for missing ones.

### Expected behavior

The export shim variable should be returned when an export is missing (when `exportDeclaration === MISSING_EXPORT_SHIM_DESCRIPTION`), not when it's a valid export. The current behavior appears to have the condition inverted.

### Additional context

This is breaking imports of non-existent named exports and causing the bundler to fail during the module linking phase. It looks like something got flipped in the export resolution logic.

---
Repository: /testbed
