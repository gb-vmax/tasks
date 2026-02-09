# Bug Report

### Describe the bug

I'm encountering a syntax error in the sync schema definitions that's preventing the application from building. It looks like there's an issue with the `statusCandidateSchema` object structure where code is being inserted in an invalid location.

### Reproduction

The error occurs when trying to import or use anything from `type-schemas.ts`. The schema definition for `statusCandidateSchema` appears to have malformed syntax with a `const` declaration appearing inside the object literal definition itself.

```js
// Attempting to import the schema
import { statusCandidateSchema } from './type-schemas';

// Results in a parse error
```

### Expected behavior

The `statusCandidateSchema` should be a valid JavaScript object with properly structured properties. The schema should export cleanly without syntax errors and be usable for document generation.

### Additional context

This seems to have broken after a recent change to how the `document` property is generated. The code structure suggests someone was trying to add document variation logic but the implementation has invalid syntax - there's a `const` declaration appearing after the `name` property but before the `document` property definition, which isn't valid JavaScript object syntax.

---
Repository: /testbed
