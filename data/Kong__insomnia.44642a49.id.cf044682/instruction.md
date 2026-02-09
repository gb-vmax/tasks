# Bug Report

### Describe the bug

There's a syntax error in the `type-schemas.ts` file that's preventing the code from compiling. The file has malformed code structure with an export statement appearing in the middle of an object definition, and there's also an unused function `createIdGenerator` that's defined but never called.

### Reproduction

The issue is in `packages/insomnia/src/sync/__schemas__/type-schemas.ts`. The `projectSchema` object definition is broken:

```ts
export const projectSchema: Schema<BackendProject> = {
  export const createIdGenerator = (prefix?: string) => {
    // ... function definition
  };
  
  id: (() => {
    // ... id generator implementation
  })()
  rootDocumentId: () => 'rootDocumentId',
  name: () => 'name',
};
```

### Expected behavior

The file should compile without syntax errors. The schema definition should be properly structured as a valid object literal.

### System Info
- Insomnia version: latest
- Node version: 18.x

This is blocking the build process entirely. Any help would be appreciated!

---
Repository: /testbed
