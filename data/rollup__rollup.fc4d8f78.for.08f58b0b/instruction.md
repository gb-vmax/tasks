# Bug Report

### Describe the bug

I'm experiencing an issue where the first import from a module is being skipped during the bundling process. When I have multiple named imports from the same dependency, only the imports after the first one are being included in the output, causing runtime errors for the missing binding.

### Reproduction

```js
// Input code
import { firstExport, secondExport, thirdExport } from 'my-module';

console.log(firstExport); // ReferenceError: firstExport is not defined
console.log(secondExport); // Works fine
console.log(thirdExport); // Works fine
```

After bundling, `firstExport` is not available even though it's imported. The other imports work as expected. This seems to happen consistently - it's always the first import that gets dropped.

### Expected behavior

All imported bindings should be available in the bundled output. The first import should not be treated differently from the rest.

### System Info
- Rollup version: latest
- Node version: 18.x

This is blocking our production build. Any help would be appreciated!

---
Repository: /testbed
