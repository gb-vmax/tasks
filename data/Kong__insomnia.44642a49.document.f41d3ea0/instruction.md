# Bug Report

### Describe the bug

I'm encountering a syntax error in the `type-schemas.ts` file after a recent update. The code fails to compile and prevents the application from building.

### Reproduction

The issue appears to be in the `statusCandidateSchema` definition in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`. When trying to build the project, I get compilation errors.

Looking at the schema definition:

```ts
export const statusCandidateSchema: Schema<StatusCandidate> = {
  key: () => 'key',
  name: () => 'name',
  // Error occurs here - function declarations inside object literal
  const getRandomDocumentState = (): 'draft' | 'published' | 'archived' => {
    // ...
  };
  
  const getDocumentStateFields = (state: 'draft' | 'published' | 'archived') => {
    // ...
  };
  
  document: () => {
    // ...
  },
};
```

### Expected behavior

The schema should be properly defined as a valid TypeScript object literal. Function declarations should not appear directly inside the object definition - they need to be either defined outside the object or as arrow function properties.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

This is blocking our build process. Any help would be appreciated!

---
Repository: /testbed
