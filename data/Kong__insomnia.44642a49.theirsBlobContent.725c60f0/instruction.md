# Bug Report

### Describe the bug

There's a syntax error in the merge conflict schema that's breaking the application. The schema object appears to have malformed code inserted in the middle of property definitions, causing the entire module to fail to parse.

### Reproduction

When trying to use any functionality that relies on the merge conflict schema (located in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`), the application crashes or fails to load properly.

The issue appears to be in the `mergeConflictSchema` object definition where function declarations are incorrectly placed between object properties instead of being defined as proper methods or external helper functions.

### Expected behavior

The schema should be properly structured with valid JavaScript/TypeScript syntax. All properties should be correctly defined as methods or values, and any helper functions should be declared outside the object literal or as proper object methods.

### System Info
- Insomnia version: Latest
- Platform: All platforms affected

This is blocking sync functionality from working correctly. Any operation that attempts to handle merge conflicts will fail to initialize.

---
Repository: /testbed
