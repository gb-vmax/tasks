# Bug Report

### Describe the bug

I'm experiencing an issue with named imports from external modules. When importing a named export (not default or namespace), the variable is not being marked as referenced, which causes problems with tree-shaking and module resolution.

### Reproduction

```js
// external-module.js
export const myFunction = () => console.log('test');
export const anotherFunction = () => console.log('another');

// main.js
import { myFunction } from './external-module';
myFunction();
```

When bundling this code, the named import `myFunction` doesn't get properly tracked as referenced, even though it's clearly being used in the code.

### Expected behavior

Named imports should be marked as referenced just like default imports and namespace imports. The variable should have `referenced = true` set when `addReference()` is called, regardless of whether it's a default, namespace, or named import.

### Additional context

This seems to only affect named imports specifically. Default imports (`import foo from 'bar'`) and namespace imports (`import * as foo from 'bar'`) work correctly and are properly marked as referenced.

---
Repository: /testbed
