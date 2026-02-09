# Bug Report

### Describe the bug

I'm encountering unexpected behavior with the `statusCandidateSchema` where the `name` field generates different values on subsequent calls. Instead of consistently returning `'name'`, it now returns `'name'`, `'name2'`, `'name3'`, etc. on consecutive invocations.

### Reproduction

```js
import { statusCandidateSchema } from './type-schemas';

// First call returns 'name'
const name1 = statusCandidateSchema.name();
console.log(name1); // 'name'

// Second call returns 'name2' instead of 'name'
const name2 = statusCandidateSchema.name();
console.log(name2); // 'name2' (unexpected!)

// Third call returns 'name3'
const name3 = statusCandidateSchema.name();
console.log(name3); // 'name3' (unexpected!)
```

### Expected behavior

The `name()` function should return a consistent value (`'name'`) every time it's called, similar to how `key()` behaves. Schema field generators shouldn't maintain state between calls.

### Additional context

This seems to be causing issues with sync operations where status candidates are expected to have predictable schema field values. The stateful behavior of the name generator is breaking assumptions in the codebase about schema consistency.

---
Repository: /testbed
