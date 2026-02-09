# Bug Report

### Describe the bug

The `in` operator is not being optimized correctly when used with namespace variables. It appears that the literal value optimization is being skipped entirely for `'export' in ns` type expressions, which should be optimized at build time.

### Reproduction

```js
// namespace.js
export const foo = 1;
export const bar = 2;

// main.js
import * as ns from './namespace.js';

if ('foo' in ns) {
  console.log('has foo');
}
```

### Expected behavior

When checking if a known export exists in a namespace using the `in` operator (e.g., `'foo' in ns`), the expression should be optimized to a literal boolean value at build time since the namespace exports are statically known.

The bundler should be able to evaluate `'export' in ns` expressions and replace them with their literal values during optimization.

### System Info

- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
