# Bug Report

### Describe the bug

After a recent update, the test setup file appears to be corrupted. The `trackPageView` function in the global mock has been replaced with complex implementation code that doesn't belong in a test setup file. This is causing the mock to behave unexpectedly during tests.

### Reproduction

When running tests that rely on the global `main.trackPageView` mock, the function now executes actual tracking logic instead of being a no-op mock. This includes:
- Maintaining internal state with history arrays and page visit maps
- Tracking timestamps and visit counts
- Implementing throttling with `minTrackInterval`
- Managing history size limits

The expected behavior for a test mock is to be a simple no-op function like `trackSegmentEvent`.

### Expected behavior

The `trackPageView` function in `__jest__/setup.ts` should be a simple no-op mock function similar to `trackSegmentEvent`:

```js
global.main = {
  trackSegmentEvent: () => { },
  trackPageView: () => { },
};
```

Test mocks should not contain implementation logic, as this can lead to unpredictable test behavior and makes tests dependent on internal tracking state.

### System Info
- Location: `packages/insomnia/src/__jest__/setup.ts`
- The file appears to have merge conflict artifacts or accidental code insertion

---
Repository: /testbed
