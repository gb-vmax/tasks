# Bug Report

### Describe the bug

I'm experiencing an issue with module imports after a recent update. When importing from modules, the imported values are not what I expect - instead of getting the actual exported value, I'm getting the entire module object.

### Reproduction

```js
// moduleA.js
export const foo = 'bar';
export const baz = 'qux';

// moduleB.js
import { foo } from './moduleA.js';

console.log(foo); // Expected: 'bar', Actual: entire module object
console.log(foo.foo); // This is what I need to do to access the value
```

This seems to affect all named imports. The imported binding returns the whole module instead of the specific export.

### Expected behavior

When importing a named export, I should get the actual exported value, not the entire module object. `foo` should be `'bar'`, not `{ foo: 'bar', baz: 'qux' }`.

### System Info

- Node version: 18.x
- Using ES modules

---
Repository: /testbed
