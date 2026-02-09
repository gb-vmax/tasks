# Bug Report

### Describe the bug

I'm encountering a syntax error in the sync schema definitions that's preventing the application from building. It looks like there's invalid JavaScript/TypeScript syntax in the `statusCandidateSchema` object definition.

### Reproduction

The error occurs when trying to build or import the type schemas module. The `statusCandidateSchema` definition appears to have code outside of the object literal structure, causing a parsing failure.

Looking at the file `packages/insomnia/src/sync/__schemas__/type-schemas.ts`, the schema definition seems malformed:

```ts
export const statusCandidateSchema: Schema<StatusCandidate> = {
  // Variable declarations and function definitions appear here
  // but they're not valid inside an object literal
  key: () => generateUniqueKey('snapshot')
  name: () => 'name',
  document: () => createBuilder(baseModelSchema).build(),
};
```

### Expected behavior

The schema should be properly structured as a valid TypeScript object literal. Variable declarations and helper functions should either be:
1. Defined outside the object literal, or
2. Properly structured within the object definition

The application should build successfully without syntax errors.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
