# Bug Report

### Describe the bug

After a recent update, the analytics tracking system seems to have broken. The `trackSegmentEvent` function is no longer working as expected and appears to be causing issues with event tracking throughout the application.

### Reproduction

```js
// Try to track a simple event
global.main.trackSegmentEvent('button_clicked', { buttonId: 'submit' });

// The event tracking doesn't work anymore
// Previously this would just no-op silently, but now something is broken
```

### Expected behavior

The `trackSegmentEvent` function should accept event names and properties without throwing errors or breaking the application flow. It should work as a simple no-op function in the test environment.

### Additional context

This appears to be related to changes in the test setup configuration. The tracking function used to be a simple empty function but now has more complex behavior that might be causing issues.

The problem manifests when trying to:
1. Track events with various property types
2. Call the function multiple times in succession
3. Use it in different parts of the test suite

### System Info
- Package: insomnia
- Environment: Jest test setup

---
Repository: /testbed
