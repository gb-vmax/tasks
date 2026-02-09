# Bug Report

### Describe the bug

After a recent update, the `trackSegmentEvent` function in the test setup is throwing a syntax error and preventing tests from running. It looks like there's a malformed object structure in the `global.main` configuration.

### Reproduction

When trying to run any test that uses the test setup, the following error occurs:

```
SyntaxError: Unexpected token 'trackSegmentEvent'
```

The issue appears to be in `packages/insomnia/src/__jest__/setup.ts` where the `global.main` object is defined. The object structure seems to be broken - there are function definitions outside of the object literal syntax.

### Expected behavior

Tests should initialize properly without syntax errors. The `global.main` object should be properly structured with all its methods correctly defined within the object literal.

### System Info
- Node version: 18.x
- Package: insomnia

This is blocking all test execution, so any help would be appreciated!

---
Repository: /testbed
