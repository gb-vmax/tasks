# Bug Report

### Describe the bug

The `describeChanges` function appears to have syntax errors or incomplete code that breaks the build. When trying to use the VCS utilities, the application fails to compile/run properly.

### Reproduction

The issue occurs when the sync/vcs utilities are loaded. The `describeChanges` function in `packages/insomnia/src/sync/vcs/util.ts` has malformed code that prevents the module from being properly parsed.

Steps to reproduce:
1. Try to import or use anything from the VCS util module
2. The application fails to start or compile

### Expected behavior

The `describeChanges` function should be properly structured and the module should load without errors. The function should be able to detect and describe changes between two objects as it did before.

### Additional context

This seems to have broken after a recent change to the util.ts file. The function definition appears to be duplicated or improperly nested, causing parsing issues.

---
Repository: /testbed
