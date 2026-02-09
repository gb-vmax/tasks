# Bug Report

### Describe the bug

I'm encountering a syntax error in the merge conflict schema file. The code appears to have malformed structure where function definitions are placed outside of the schema object, breaking the expected schema format.

### Reproduction

When trying to use the merge conflict functionality:

```js
import { mergeConflictSchema } from './type-schemas';

// Attempting to create or access merge conflict data
const conflict = createBuilder(mergeConflictSchema).build();
```

This results in a syntax error because the schema object is not properly closed before new function definitions are added.

### Expected behavior

The `mergeConflictSchema` should be a valid schema object with all properties properly defined within the object literal. Helper functions like `simpleHash`, `getContentType`, and `generateMockBlobContent` should either be defined outside the schema or the schema should be properly structured to allow their use.

### System Info
- Node version: 18.x
- Package: @insomnia/sync

The issue seems to be in the type-schemas.ts file where the schema object structure got corrupted - there are function definitions appearing in the middle of the object literal definition which causes a parsing error.

---
Repository: /testbed
