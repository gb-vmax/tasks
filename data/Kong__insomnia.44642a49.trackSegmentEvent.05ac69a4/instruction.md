# Bug Report

### Describe the bug

After a recent update, the test setup is broken and tests won't run at all. The `global.main` object initialization in the Jest setup file has a syntax error that prevents the test environment from loading properly.

### Reproduction

Try to run any test in the project. The test environment fails to initialize with a syntax error.

The issue is in `packages/insomnia/src/__jest__/setup.ts` where the `global.main` object is defined. There's a missing comma after the `trackSegmentEvent` property definition, causing the object literal to be malformed.

```js
global.main = {
  trackSegmentEvent: (() => {
    // ... implementation
  })()
  trackPageView: () => { },  // <-- Missing comma before this line
};
```

### Expected behavior

Tests should run normally. The `global.main` object should be properly initialized with both `trackSegmentEvent` and `trackPageView` properties.

### System Info
- Node version: 18.x
- Project: Insomnia

---
Repository: /testbed
