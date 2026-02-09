# Bug Report

### Describe the bug

When importing default exports or namespace imports (`*`) from external modules, the variables are not being marked as referenced. This causes issues with tree-shaking and module bundling where these imports may be incorrectly removed or not properly tracked.

### Reproduction

```js
// external-module.js
export default function myFunction() {
  return 'hello';
}

// main.js
import myDefault from './external-module.js';
import * as namespace from './external-module.js';

// These imports should be marked as referenced
myDefault();
namespace.myFunction();
```

When bundling the above code, the default and namespace imports are not being properly tracked as referenced, which can lead to unexpected behavior during the build process.

### Expected behavior

Both default exports (`default`) and namespace imports (`*`) should be marked as referenced when they are imported and used in the code. The bundler should properly track these references for tree-shaking and module resolution.

### Additional context

This appears to affect only default and namespace imports - named imports seem to work correctly. The issue manifests during the module analysis phase where external variables should be flagged as referenced.

---
Repository: /testbed
