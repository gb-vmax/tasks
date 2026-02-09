# Bug Report

### Describe the bug

There's a syntax error in the `type-schemas.ts` file that's preventing the application from compiling. The `backendProjectWithTeamSchema` definition appears to have malformed code where a function definition is placed in the middle of an object literal without proper syntax.

### Reproduction

The issue occurs when trying to import or use anything from `packages/insomnia/src/sync/__schemas__/type-schemas.ts`. The file won't parse correctly due to invalid JavaScript/TypeScript syntax.

Looking at the schema definition:
```ts
export const backendProjectWithTeamSchema: Schema<BackendProjectWithTeam> = {
  ...projectSchema,
  function mergeSchemaWithOverrides<T>(...) { ... }  // This is invalid syntax
  team: (context?: { teamOverrides?: Partial<Team> }) => { ... }
};
```

The `mergeSchemaWithOverrides` function is defined inside the object literal without being assigned to a property, which causes a parsing error.

### Expected behavior

The file should compile without syntax errors. If a helper function is needed, it should be defined outside the object literal or properly assigned as a method.

### System Info
- Package: @insomnia/insomnia
- Location: `packages/insomnia/src/sync/__schemas__/type-schemas.ts`

---
Repository: /testbed
