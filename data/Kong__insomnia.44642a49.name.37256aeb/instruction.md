# Bug Report

### Describe the bug

I'm encountering a syntax error in the sync schema definitions. It looks like there's some malformed code in the `statusCandidateSchema` object where the `name` property definition is broken. The code won't compile/parse at all.

### Reproduction

When trying to use or import the schema, I get a syntax error. The `statusCandidateSchema` appears to have invalid JavaScript/TypeScript syntax - there's code that looks like it's outside of the object structure and the `name` property definition is incomplete.

Looking at the code in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`, the schema object structure seems corrupted:

```ts
export const statusCandidateSchema: Schema<StatusCandidate> = {
  key: () => 'key',
  // ... broken syntax here
  name: () => { /* ... */ }
  document: () => createBuilder(baseModelSchema).build(),
};
```

### Expected behavior

The schema should be properly structured with valid JavaScript/TypeScript syntax and should compile without errors.

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
