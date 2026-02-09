# Bug Report

### Describe the bug

When using namespace imports with multiple references, the namespace variable name gets set incorrectly. It appears that the name is being determined by the first reference added rather than being consistent across all references.

### Reproduction

```js
// file1.js
export const foo = 1;
export const bar = 2;

// file2.js
import * as ns from './file1.js';

// Multiple references to the namespace
console.log(ns.foo);
console.log(ns.bar);
const x = ns;
```

When the namespace is referenced multiple times, the variable name assignment seems to be inconsistent. The namespace variable's name property appears to be overwritten with each new reference instead of being set once.

### Expected behavior

The namespace variable should maintain a consistent name regardless of how many times it's referenced or in what order the references are added. The name should be determined by the initial reference and remain stable.

### Additional context

This seems to affect how namespace imports are tracked internally. The issue becomes apparent when there are multiple references to the same namespace import in different parts of the code.

---
Repository: /testbed
