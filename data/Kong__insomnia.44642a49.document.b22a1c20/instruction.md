# Bug Report

### Describe the bug

There's a syntax error in the `statusCandidateSchema` definition that prevents the code from compiling. The schema object has malformed structure with interface and function definitions appearing in the middle of the object literal.

### Reproduction

When trying to import or use anything from `type-schemas.ts`, the module fails to load due to a parse error. The `statusCandidateSchema` object is corrupted:

```ts
export const statusCandidateSchema: Schema<StatusCandidate> = {
  key: () => 'key',
  name: () => 'name',
  interface DocumentBuildContext {  // This shouldn't be here
    // ...
  }
  // ...
  document: () => { /* ... */ }
};
```

The interface `DocumentBuildContext` and related helper code are declared inside the schema object literal instead of outside it, causing a syntax error.

### Expected behavior

The code should compile successfully. Type definitions and helper functions should be declared outside of object literals at the module level.

### System Info
- Insomnia sync module
- TypeScript compilation fails on this file

---
Repository: /testbed
