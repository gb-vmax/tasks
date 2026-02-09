# Bug Report

### Describe the bug

I'm encountering a syntax error in the `type-schemas.ts` file that's preventing the application from building. It looks like there's invalid code in the `snapshotStateEntrySchema` object definition where function declarations appear in the middle of an object literal.

### Reproduction

The issue appears in `packages/insomnia/src/sync/__schemas__/type-schemas.ts` in the `snapshotStateEntrySchema` definition. When trying to build or run the application, it fails due to malformed syntax.

The schema object has:
```ts
export const snapshotStateEntrySchema: Schema<SnapshotStateEntry> = {
  blob: () => 'blob',
  key: () => 'key',
  // ... then function declarations appear here which breaks the object syntax
```

### Expected behavior

The `snapshotStateEntrySchema` object should be properly formatted with valid JavaScript/TypeScript syntax. Object properties should be defined correctly without mixing in standalone function declarations.

### System Info
- Node version: Latest
- TypeScript: 4.x+

This is blocking the build process completely. Any help would be appreciated!

---
Repository: /testbed
