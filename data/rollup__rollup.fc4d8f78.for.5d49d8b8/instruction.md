# Bug Report

### Describe the bug

I'm experiencing an issue where the last import from a module is not being included in the generated bundle. When importing multiple named exports from a dependency, only the first n-1 imports are actually processed, and the final import is silently dropped.

### Reproduction

```js
// Source code
import { foo, bar, baz } from 'my-module';

console.log(foo, bar, baz);
```

After bundling, only `foo` and `bar` are available in the output. The `baz` import is missing from the generated code, which causes a ReferenceError at runtime.

### Expected behavior

All named imports from a module should be included in the bundle, not just the first n-1 imports. The last import should be processed the same way as all the others.

### Additional context

This appears to affect any module with multiple named imports. The pattern is consistent - if you import 3 things, only 2 are included. If you import 5 things, only 4 are included, etc.

---
Repository: /testbed
