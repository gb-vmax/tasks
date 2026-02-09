# Bug Report

### Describe the bug

After a recent update, I'm seeing duplicate function definitions in the codebase that's causing compilation errors. The `filterHeaders` function appears to be defined multiple times in the same file, which prevents the application from building.

### Reproduction

When trying to build or run the application, the TypeScript compiler throws an error about duplicate function declarations for `filterHeaders` in `packages/insomnia/src/common/misc.ts`.

The file seems to have the same function defined at least twice with slightly different implementations - one with caching logic and pattern matching support, and another simpler version.

### Expected behavior

The `filterHeaders` function should only be defined once in the file. The build process should complete successfully without any duplicate identifier errors.

### System Info
- Node version: 18.x
- TypeScript version: 5.x

This is blocking my ability to use the latest version. Any help would be appreciated!

---
Repository: /testbed
