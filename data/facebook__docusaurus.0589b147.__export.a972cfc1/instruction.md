# Bug Report

### Describe the bug

I'm experiencing an issue where exported module properties are not accessible correctly. When trying to access exported functions or values from a module, all exports seem to reference the same value instead of their respective implementations.

### Reproduction

```js
// module.js exports multiple functions
export function foo() { return 'foo' }
export function bar() { return 'bar' }
export function baz() { return 'baz' }

// consumer.js
import { foo, bar, baz } from './module.js'

console.log(foo()) // Expected: 'foo', Actual: returns same value as bar
console.log(bar()) // Expected: 'bar', Actual: all exports return the same thing
console.log(baz()) // Expected: 'baz', Actual: same issue
```

All the exported functions seem to be pointing to the same reference rather than their individual implementations. This makes it impossible to use multiple exports from the same module.

### Expected behavior

Each exported function/value should maintain its own identity and be accessible independently. When importing multiple named exports, they should work as distinct entities.

### System Info
- Node version: 18.x
- Using bundled modules

---
Repository: /testbed
