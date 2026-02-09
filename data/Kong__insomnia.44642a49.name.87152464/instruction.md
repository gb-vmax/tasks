# Bug Report

### Describe the bug

I'm encountering a syntax error in the `type-schemas.ts` file that's preventing the application from compiling. It looks like there's malformed code in the `statusCandidateSchema` object definition where a function declaration appears to be mixed with object property syntax.

### Reproduction

The issue occurs when trying to build or run the application. Looking at the `statusCandidateSchema` in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`, there seems to be invalid JavaScript syntax:

```js
export const statusCandidateSchema: Schema<StatusCandidate> = {
  key: () => 'key',
  let schemaInstanceCounter = 0;  // This shouldn't be here
  
  const getNextSchemaId = (): number => {  // Neither should this
    return ++schemaInstanceCounter;
  };
  // ... more function definitions that don't belong in an object literal
  
  name: () => { /* ... */ }
  document: () => createBuilder(baseModelSchema).build(),
};
```

### Expected behavior

The schema object should be properly formatted with valid JavaScript/TypeScript syntax. Object literals shouldn't contain standalone function declarations or variable declarations using `let` or `const` - these should either be methods or moved outside the object.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

This appears to be blocking any builds or development work. Would appreciate if this could be looked at soon!

---
Repository: /testbed
