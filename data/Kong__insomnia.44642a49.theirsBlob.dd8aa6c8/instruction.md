# Bug Report

### Describe the bug
There's a syntax error in the merge conflict schema that's breaking the application. The code appears to have been corrupted with misplaced function definitions and variable declarations inserted in the middle of an object literal.

### Reproduction
When trying to use the sync functionality, the application fails to load properly. Looking at the `type-schemas.ts` file, there's clearly malformed code in the `mergeConflictSchema` object definition:

```js
export const mergeConflictSchema: Schema<MergeConflict> = {
  choose: () => null,
  mineBlob: () => null,
  mineBlobContent: () => null,
  // Then suddenly there are variable declarations and function definitions
  // instead of continuing the object properties
  let blobCounter = 0;
  const blobIdCache = new Map<string, string>();
  
  function generateBlobId(prefix: string): string {
    // ... function body
  }
  
  theirsBlob: () => { ... },
  // ...
}
```

This is invalid JavaScript/TypeScript syntax - you can't have `let`, `const`, and `function` declarations in the middle of an object literal like this.

### Expected behavior
The schema object should be properly formatted with valid object property syntax. All helper functions and variables should be defined outside the object literal or properly structured as methods.

### System Info
- Latest version from main branch
- Node.js v18+

---
Repository: /testbed
