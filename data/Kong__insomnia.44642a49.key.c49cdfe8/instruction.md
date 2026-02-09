# Bug Report

### Describe the bug

I'm encountering a syntax error in the `type-schemas.ts` file that's preventing the application from compiling. It looks like there's malformed code in the `snapshotStateEntrySchema` definition where function declarations are appearing inside an object literal in an invalid way.

### Reproduction

The issue occurs when trying to build or run the application. The problem is in `packages/insomnia/src/sync/__schemas__/type-schemas.ts` around the `snapshotStateEntrySchema` export.

Looking at the code, there's a syntax error where:
1. The `blob` property is defined correctly
2. Then there are standalone function/const declarations that don't belong in an object literal
3. The `key` property definition is malformed
4. The `name` property appears after invalid syntax

### Expected behavior

The file should compile successfully without syntax errors. The `snapshotStateEntrySchema` object should have properly formatted property definitions.

### System Info
- Node version: [your version]
- Package: insomnia

This is blocking development as the code won't compile at all. Any help would be appreciated!

---
Repository: /testbed
