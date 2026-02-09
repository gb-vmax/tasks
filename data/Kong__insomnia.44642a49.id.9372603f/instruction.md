# Bug Report

### Describe the bug

After a recent update, I'm getting a syntax error in the `type-schemas.ts` file. The application fails to compile and throws an error about unexpected token near the `teamSchema` definition.

### Reproduction

The issue appears to be in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`. When trying to build or run the application, it fails with a parsing error around the schema definition.

```ts
export const teamSchema: Schema<Team> = {
  // ... code attempts to define functions and state before the object properties
  id: () => { ... },
  name: () => 'teamName',
};
```

### Expected behavior

The schema should be properly defined as a valid TypeScript/JavaScript object and the application should compile successfully.

### System Info
- Node version: Latest
- TypeScript version: Latest

The code structure looks malformed - it seems like some state management code and helper functions were accidentally placed inside the schema object definition instead of outside it.

---
Repository: /testbed
