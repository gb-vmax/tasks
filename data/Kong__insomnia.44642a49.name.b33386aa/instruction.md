# Bug Report

### Describe the bug

I'm experiencing a syntax error in the type-schemas.ts file that's preventing the application from building. The code appears to have malformed structure with variable declarations and function definitions placed outside of the schema object definition.

### Reproduction

When trying to build or run the application, the following code in `packages/insomnia/src/sync/__schemas__/type-schemas.ts` causes a syntax error:

```typescript
export const teamSchema: Schema<Team> = {
  id: () => 'teamId',
  name: () => 'teamName',
};
```

It looks like there's an attempt to add some team name generation logic, but the code structure is broken - there are `let` declarations and function definitions that appear to be inserted in the middle of the object literal, which is invalid JavaScript/TypeScript syntax.

### Expected behavior

The schema should be properly defined with valid TypeScript syntax and the application should build successfully. If unique team name generation is needed, the helper variables and functions should be declared outside the schema object.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
