# Bug Report

### Describe the bug

I'm encountering an issue where declaring a variable with the same name as an imported module member is not being caught as an error. The bundler should throw a redeclaration error when trying to declare a variable that conflicts with an import, but it's allowing it through instead.

### Reproduction

```js
import { foo } from './module.js';

// This should throw a redeclaration error but doesn't
const foo = 'bar';

console.log(foo);
```

Expected: Rollup should catch this and throw a redeclaration error since `foo` is already imported.

Actual: The code passes through without any error being raised.

### Expected behavior

When a variable is declared with the same name as an imported identifier, Rollup should detect this conflict and throw a redeclaration error to prevent shadowing imports.

### Additional context

This seems to have started happening recently. Previously, these kinds of naming conflicts were properly detected and reported as errors during the build process.

---
Repository: /testbed
