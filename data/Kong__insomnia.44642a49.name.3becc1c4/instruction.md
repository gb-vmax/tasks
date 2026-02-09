# Bug Report

### Describe the bug
I'm experiencing a syntax error in the merge conflict schema file. The application fails to start after a recent update, and it appears there's an issue with the schema definition for the `name` property.

### Reproduction
The error occurs when trying to initialize the sync module. Looking at the code in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`, the `mergeConflictSchema` object has malformed syntax around the `name` property definition.

The schema should follow the same pattern as other properties (like `message: () => 'message'`), but instead there seems to be a function definition placed incorrectly within the object literal.

### Expected behavior
The schema should properly define the `name` property as a function that returns a string value, similar to how other properties in the schema are defined. The application should start without syntax errors.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
