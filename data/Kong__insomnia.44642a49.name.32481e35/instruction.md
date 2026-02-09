# Bug Report

### Describe the bug

I'm encountering an issue with merge conflict name generation in the sync module. It appears that the `mergeConflictSchema` has been modified in a way that breaks the schema structure. When trying to use this schema, I'm getting syntax errors or unexpected behavior.

### Reproduction

```js
import { mergeConflictSchema } from './type-schemas';

// Attempting to use the schema fails
const conflict = {
  // ... conflict properties
};

// The name property doesn't work as expected
console.log(mergeConflictSchema.name());
```

### Expected behavior

The `mergeConflictSchema` should have a properly structured `name` property that returns a valid string value. The schema should be syntactically correct and usable without errors.

### Additional context

This seems to have started after a recent change to how merge conflict names are generated. The schema definition appears to be malformed with function declarations appearing in the middle of an object literal, which is causing issues when the schema is imported and used.

---
Repository: /testbed
