# Bug Report

### Describe the bug

After a recent update, the schema generation for projects is producing inconsistent IDs. The `projectSchema` object is returning IDs with unexpected prefixes like `project-1`, `project-2` instead of the simple `'id'` string that was previously returned.

### Reproduction

```js
import { projectSchema } from './type-schemas';

// Expected: 'id'
// Actual: 'project-1' (or similar with counter)
const id1 = projectSchema.id();
console.log(id1); // prints something like 'project-1'

const id2 = projectSchema.id();
console.log(id2); // prints something like 'project-2'
```

### Expected behavior

The `projectSchema.id()` function should consistently return the string `'id'` as it did before. The schema is supposed to define the structure/shape of the data, not generate unique IDs with counters and prefixes.

### Additional context

This seems to have broken after some changes to the schema definitions. The code now includes logic for generating unique IDs with prefixes and counters, but this appears to be interfering with the basic schema definition functionality. Multiple calls to `projectSchema.id()` are returning different values each time, which breaks assumptions in code that expects a consistent schema shape.

---
Repository: /testbed
