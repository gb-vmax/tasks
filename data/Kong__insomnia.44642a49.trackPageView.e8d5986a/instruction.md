# Bug Report

### Describe the bug

After a recent update, the test setup file appears to have a syntax error that's breaking the build. The `global.main` object definition seems to be malformed with missing closing braces and incorrect placement of function definitions.

### Reproduction

The issue is in the test setup file (`packages/insomnia/src/__jest__/setup.ts`). When trying to run the application or tests, it fails to parse due to syntax errors in the global.main object structure.

The problem appears to be:
1. Missing closing brace for the `global.main` object
2. Function definitions like `_generateSessionId`, `getPageViewHistory`, `clearPageViewHistory`, and `setPageViewRateLimit` are defined outside the object literal
3. The `trackPageView` property is defined without proper object syntax

### Expected behavior

The `global.main` object should be properly structured with all methods defined as properties of the object, with correct syntax and closing braces.

### System Info
- Node version: Latest
- Package: insomnia

This is blocking development as the setup file won't parse correctly. Any help would be appreciated!

---
Repository: /testbed
