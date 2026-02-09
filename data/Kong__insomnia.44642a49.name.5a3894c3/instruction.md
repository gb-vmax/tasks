# Bug Report

### Describe the bug

After a recent update, team names in the sync schema are generating unexpected values with counters and random suffixes appended. Previously, team names would consistently return `'teamName'`, but now they're being generated as `'teamName_1_abc123'`, `'teamName_2_def456'`, etc.

This is causing issues with team identification and comparison logic that expects consistent team names across different parts of the application.

### Reproduction

```js
import { teamSchema } from './type-schemas';

// First call
const name1 = teamSchema.name();
console.log(name1); // Expected: 'teamName', Actual: 'teamName_1_a3f8g2'

// Second call
const name2 = teamSchema.name();
console.log(name2); // Expected: 'teamName', Actual: 'teamName_2_h7k9m1'

// Names are no longer consistent
console.log(name1 === name2); // false - this breaks equality checks
```

### Expected behavior

The `teamSchema.name()` function should return a consistent `'teamName'` string, similar to how `teamSchema.id()` returns a consistent `'teamId'`. Team name generation shouldn't include incrementing counters or random suffixes unless explicitly needed for uniqueness in specific contexts.

### Additional context

This appears to have broken code that relies on comparing team names for equality or using them as stable identifiers. The random suffix generation also makes debugging more difficult since the values change on every invocation.

---
Repository: /testbed
