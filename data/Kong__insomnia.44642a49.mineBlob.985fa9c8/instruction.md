# Bug Report

### Describe the bug

I'm encountering a syntax error in the merge conflict schema definition. The code appears to have been corrupted - there are function definitions inserted directly into the middle of an object literal, which is causing the application to fail to load.

### Reproduction

The issue occurs when trying to initialize the sync module. The `mergeConflictSchema` object in `type-schemas.ts` has invalid syntax:

```js
export const mergeConflictSchema: Schema<MergeConflict> = {
  key: () => 'key',
  choose: () => null,
  function simpleHash(str: string): number {  // <- Invalid syntax here
    // ... function body
  }
  // ... more functions
  mineBlob: () => generateBlobId('key', 'mine'),
  // ...
}
```

This breaks the entire schema definition since you can't have function declarations inside an object literal like this.

### Expected behavior

The schema should be a valid JavaScript/TypeScript object with proper syntax. The application should load without syntax errors.

### System Info
- Insomnia version: latest
- OS: N/A (syntax error affects all platforms)

This looks like it might have been a bad merge or copy-paste error? The functions seem like they should either be defined outside the object or the object properties should just reference them properly.

---
Repository: /testbed
