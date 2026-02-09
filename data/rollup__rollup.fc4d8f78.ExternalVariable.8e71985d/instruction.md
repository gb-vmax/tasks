# Bug Report

### Describe the bug

I'm experiencing an issue with module name suggestions for external variables. When importing the default export or namespace import from an external module, the suggested name from the identifier is being applied incorrectly. It seems like the name suggestion logic is inverted - it's suggesting names when it shouldn't and not suggesting them when it should.

### Reproduction

```js
// When importing default export
import myCustomName from 'external-module';

// Expected: Should NOT suggest 'myCustomName' as the module name
// Actual: The module name is being suggested from the identifier

// When importing named exports
import { someExport } from 'external-module';

// Expected: Should suggest 'someExport' as the module name
// Actual: No name suggestion is being made
```

### Expected behavior

- For default exports (`default`) and namespace imports (`*`), the identifier name should NOT be used to suggest the module name
- For named exports, the identifier name SHOULD be used to suggest the module name

### Additional context

This appears to affect how external modules are named/referenced in the bundled output. The current behavior is backwards from what it should be.

---
Repository: /testbed
