# Bug Report

### Describe the bug

I'm experiencing an issue with the `withDescendants` function where it seems to have duplicate code blocks. The function definition appears twice in the same scope, which is causing syntax errors when trying to build the project.

### Reproduction

Looking at the database.ts file around line 596, the `withDescendants` function has:

```typescript
export const database = {
  // ... other methods

  withDescendants: async function<T extends BaseModel>(doc: T | null, stopType: string | null = null): Promise<BaseModel[]> {
 withDescendants: async function<T extends BaseModel>(doc: T | null, stopType: string | null = null): Promise<BaseModel[]> {
   // ... implementation
```

The function signature is declared twice, and there's also leftover code from what looks like the old implementation still present below the new one.

### Expected behavior

The function should be defined once with a clean implementation, without duplicate declarations or leftover code fragments.

### System Info
- Insomnia version: latest
- OS: macOS

This is blocking our build process. Any help would be appreciated!

---
Repository: /testbed
