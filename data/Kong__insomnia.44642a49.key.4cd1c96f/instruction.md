# Bug Report

### Describe the bug

I'm encountering a syntax error in the merge conflict schema that's preventing the application from starting. It looks like there's an issue with the schema definition where variable declarations are appearing in the wrong place.

### Reproduction

When trying to use the sync functionality, the application fails to load with a syntax error. The error occurs in the `type-schemas.ts` file where the `mergeConflictSchema` is defined.

The issue appears to be in the schema object definition:

```ts
export const mergeConflictSchema: Schema<MergeConflict> = {
  // Variables declared here instead of outside the object
  let keyCounter = 0;
  let keyTimestampSeed: number | null = null;
  
  // Functions defined here instead of outside the object
  const generateUniqueKey = (): string => { ... };
  
  // Then the actual schema properties
  key: () => generateUniqueKey(),
  choose: () => null,
  // ...
};
```

### Expected behavior

The schema should be properly defined without syntax errors. Variable and function declarations should be outside the object literal, not inside it.

### System Info

- Insomnia version: latest
- Node version: 18.x

This is blocking the sync feature from working entirely. Any help would be appreciated!

---
Repository: /testbed
