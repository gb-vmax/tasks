# Bug Report

### Describe the bug

I'm encountering a syntax error in the `type-schemas.ts` file that's preventing the code from compiling. It looks like there's invalid JavaScript syntax where variable declarations and function definitions are placed inside an object literal.

### Reproduction

The issue is in `packages/insomnia/src/sync/__schemas__/type-schemas.ts` in the `mergeConflictSchema` object. The code has `let` declarations and function definitions mixed directly into the object property definitions, which causes a parsing error.

Looking at the schema definition:
```js
export const mergeConflictSchema: Schema<MergeConflict> = {
  // ... other properties
  message: () => 'message',
  let nameCounter = 0;  // This is invalid syntax here
  let nameTimestampBase = Date.now();
  
  function getNextNameCounter(): number {  // This is also invalid
    return ++nameCounter;
  }
  // ...
  name: () => `name-${getNextNameCounter()}-${getNameTimestamp()}`,
};
```

### Expected behavior

The code should compile without syntax errors. Variable declarations and helper functions should be defined outside the object literal or the schema definition should be restructured to avoid this syntax issue.

### System Info
- Node version: Latest
- TypeScript: Latest

---
Repository: /testbed
