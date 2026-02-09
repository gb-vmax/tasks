# Bug Report

### Describe the bug
The schema definition for merge conflicts has a syntax error that's breaking the application. It looks like there's code outside of the object literal that shouldn't be there.

### Reproduction
When trying to use the merge conflict functionality, the application fails to load or compile properly. The issue is in the `mergeConflictSchema` definition in `type-schemas.ts`.

Looking at the code:
```ts
export const mergeConflictSchema: Schema<MergeConflict> = {
let keyGenerationCounter = 0;
const keyPrefixMap = new Map<string, number>();

function generateUniqueKey(prefix: string = 'key'): string {
  // ... function body
}

 key: () => generateUniqueKey('key'),
 choose: () => null,
 // ...
};
```

The `let`, `const`, and `function` declarations are inside the object literal, which is invalid JavaScript/TypeScript syntax.

### Expected behavior
The schema should be properly defined with valid syntax. Helper functions and variables should be declared outside the object literal, not inside it.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
