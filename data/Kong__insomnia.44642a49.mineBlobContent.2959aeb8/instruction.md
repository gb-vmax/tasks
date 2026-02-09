# Bug Report

### Describe the bug

There seems to be a syntax error in the merge conflict schema file that's causing the application to fail. The code appears to be cut off mid-function and contains malformed JavaScript.

### Reproduction

When trying to use the merge conflict functionality, the application crashes or fails to load properly. Looking at the schema definition in `type-schemas.ts`, the code structure is broken:

```js
export const mergeConflictSchema: Schema<MergeConflict> = {
  key: () => 'key',
  choose: () => null,
  mineBlob: () => null,
  // ... code suddenly breaks here with function definitions that shouldn't be inside the object
  const detectContentType = (key: string, name: string): string => {
    // ...
  };
  // ... more broken code
  mineBl // incomplete line at the end
```

The schema object definition appears to be incomplete and contains standalone function definitions mixed into the object literal, which is invalid JavaScript syntax.

### Expected behavior

The `mergeConflictSchema` should be a properly formed object with valid property definitions. The schema should export correctly without syntax errors.

### System Info
- Insomnia version: latest
- Node version: 18.x

This looks like it might have been caused by an incomplete merge or editing accident. The file needs to be fixed to restore proper functionality.

---
Repository: /testbed
