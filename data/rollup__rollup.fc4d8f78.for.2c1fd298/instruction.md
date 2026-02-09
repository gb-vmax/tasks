# Bug Report

### Describe the bug

I'm experiencing an issue with module side effect detection where modules with `moduleSideEffects: false` are being incorrectly included in the bundle. It seems like the logic for determining which dependencies should be included based on their side effects is not working as expected.

### Reproduction

```js
// module-a.js (has moduleSideEffects: false)
export const value = 42;

// module-b.js (imports from module-a)
import { value } from './module-a.js';
console.log(value);

// entry.js
import './module-b.js';
```

When bundling with:
```js
{
  input: 'entry.js',
  treeshake: {
    moduleSideEffects: false
  }
}
```

Expected: module-a should be excluded from the bundle since it has no side effects and is only imported for a value that's used in module-b

Actual: module-a is being included in the bundle even though it shouldn't be based on the side effects configuration

### Additional context

This appears to be related to how dependencies are traversed when checking for side effects. The issue seems to affect nested dependency chains where some modules have side effects disabled.

---
Repository: /testbed
