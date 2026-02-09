# Bug Report

### Describe the bug

I'm encountering a syntax error in the schema definitions after a recent update. The code appears to have malformed object structure where function declarations are mixed incorrectly within an object literal.

### Reproduction

When trying to use the `mergeConflictSchema`, the application fails to load due to a syntax error in the schema definition. The schema object seems to have code placed outside of its proper structure.

```js
// Attempting to use the schema results in a syntax error
import { mergeConflictSchema } from './type-schemas';

// This will fail to parse
const conflict = mergeConflictSchema.name();
```

### Expected behavior

The schema should be properly structured as a valid JavaScript object with all properties correctly defined within the object literal. The `name` property should be a simple function that can be called without errors.

### System Info
- Node version: Latest
- Package: @insomnia/sync

The error prevents the module from being imported at all, suggesting there's a structural issue with how the object is defined rather than a runtime problem.

---
Repository: /testbed
