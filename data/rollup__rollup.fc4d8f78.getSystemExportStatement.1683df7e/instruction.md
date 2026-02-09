# Bug Report

### Describe the bug

When exporting multiple named exports in SystemJS format, all exports are incorrectly pointing to the same variable instead of their respective variables. This causes all exported names to reference only the first exported variable.

### Reproduction

```js
// Input code with multiple exports
export const foo = 'foo value';
export const bar = 'bar value';
export const baz = 'baz value';

// Expected SystemJS output:
// exports({ foo: foo, bar: bar, baz: baz })

// Actual output:
// exports({ foo: foo, bar: foo, baz: foo })
```

When importing these exports:
```js
import { foo, bar, baz } from './module';

console.log(foo); // 'foo value'
console.log(bar); // 'foo value' - WRONG! Should be 'bar value'
console.log(baz); // 'foo value' - WRONG! Should be 'baz value'
```

### Expected behavior

Each exported name should reference its corresponding variable. Multiple exports should maintain their individual variable references in the generated SystemJS code.

### Additional context

This appears to affect scenarios where there are multiple exported variables with single export names each. Single export cases seem to work fine, but as soon as you have 2 or more exports, they all end up referencing the first variable.

---
Repository: /testbed
