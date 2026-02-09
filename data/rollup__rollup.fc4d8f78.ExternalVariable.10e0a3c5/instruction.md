# Bug Report

### Describe the bug

I'm experiencing an issue with external module imports where the suggested names are being applied incorrectly. When importing default exports or namespace imports (using `*`), the module is suggesting names based on the identifier, but this shouldn't be happening for these special import types.

### Reproduction

```js
// When importing a default export
import myComponent from './Component'

// Or when using namespace imports
import * as utils from './utils'
```

In both cases, the module is incorrectly suggesting names based on the identifier (`myComponent` or `utils`), when it should only suggest names for named imports.

### Expected behavior

Name suggestions should only occur for regular named imports, not for default exports or namespace imports. The current behavior is backwards - it's suggesting names for the cases where it shouldn't, and not suggesting them for regular named imports where it should.

### Additional context

This seems to affect how modules are being processed and could lead to incorrect module name resolution in the final bundle.

---
Repository: /testbed
