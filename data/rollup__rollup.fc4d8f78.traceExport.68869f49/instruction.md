# Bug Report

### Describe the bug

I'm encountering an issue with export tracing where exported variables cannot be resolved correctly. When trying to trace an export by name, it seems like the export name lookup is failing and variables are not being found.

### Reproduction

```js
// module-a.js
export const myValue = 42;
export function myFunction() {
  return 'hello';
}

// module-b.js
import { myValue, myFunction } from './module-a.js';

console.log(myValue);
console.log(myFunction());
```

When bundling these modules, the exports from `module-a.js` are not being traced properly. The build completes but the exported names don't seem to resolve to the correct variables.

### Expected behavior

The `traceExport` function should correctly locate and return the variable associated with the given export name. Imports should work as expected and the bundled output should contain the correct references.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
