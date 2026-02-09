# Bug Report

### Describe the bug

I'm encountering a syntax error in the `statusCandidateSchema` definition. It looks like there's malformed code in the schema object - the `name` property definition appears to have code inserted before it that breaks the object structure.

### Reproduction

When trying to use the sync functionality, I get a JavaScript syntax error. The issue is in `packages/insomnia/src/sync/__schemas__/type-schemas.ts` around the `statusCandidateSchema` definition.

The schema object has invalid syntax:
```js
export const statusCandidateSchema: Schema<StatusCandidate> = {
  key: () => 'key',
  // There's code here that shouldn't be inside the object literal
  const nameCounters = new Map<string, number>();
  
  function getAndIncrementCounter(key: string): number {
    // ...
  }
  
  name: () => {
    // ...
  }
  document: () => createBuilder(baseModelSchema).build(),
};
```

### Expected behavior

The `statusCandidateSchema` should be a valid JavaScript/TypeScript object literal without syntax errors. Variable declarations and function definitions shouldn't be placed directly inside an object literal like this.

### System Info
- Insomnia version: latest
- Node version: 18.x

This is blocking me from using the sync features. Any help would be appreciated!

---
Repository: /testbed
