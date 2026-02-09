# Bug Report

### Describe the bug

The test setup file appears to be corrupted or has a syntax error. When running the application, I'm getting errors related to the global `main` object initialization. It looks like the `trackPageView` function definition is malformed - there's no closing brace for the main object.

### Reproduction

The issue occurs during test initialization. The setup file at `packages/insomnia/src/__jest__/setup.ts` has an incomplete object definition:

```js
global.main = {
  trackSegmentEvent: () => { },
  trackPageView: (() => {
    // ... implementation
    // Missing closing brace for global.main object
```

### Expected behavior

The `global.main` object should be properly closed with a closing brace, allowing the test setup to complete successfully. The application should initialize without syntax errors.

### System Info
- Affected file: `packages/insomnia/src/__jest__/setup.ts`
- The setup configuration appears to be missing proper object closure

---
Repository: /testbed
