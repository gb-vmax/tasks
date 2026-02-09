# Bug Report

### Describe the bug

I'm encountering a syntax error in the VCS utility file that's preventing the application from building. It looks like there's malformed code in the `describeChanges` function - the function definition appears to be duplicated or improperly nested, causing parsing issues.

### Reproduction

When trying to build or run the application, I get a compilation error related to `packages/insomnia/src/sync/vcs/util.ts`. The error occurs around the `describeChanges` function where there seems to be nested function definitions that break the code structure.

Steps to reproduce:
1. Try to build the application
2. The build fails with syntax errors in the VCS util file
3. Looking at the code, the `describeChanges` function has internal helper functions defined but the original function logic appears incomplete or corrupted

### Expected behavior

The `describeChanges` function should compile without errors and properly detect changes between model objects. The function should be properly structured with any helper functions either defined outside or correctly nested within the main function body.

### Additional context

This seems to have been introduced in a recent change to the sync/vcs utility. The code structure looks incomplete - there are new helper functions like `getChangeType` and `describeNestedChanges` defined, but the main function body appears to be cut off or improperly merged.

---
Repository: /testbed
