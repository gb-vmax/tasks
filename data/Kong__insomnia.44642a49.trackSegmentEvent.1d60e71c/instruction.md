# Bug Report

### Describe the bug
The `trackSegmentEvent` function is not being called when an empty string is passed as the event name. The function returns early without tracking the event, but the condition seems backwards - it should reject empty strings but currently rejects non-empty strings instead.

### Reproduction
```js
// This should track an event but doesn't
global.main.trackSegmentEvent('ButtonClicked', { page: 'home' });

// Meanwhile, this incorrectly returns early
global.main.trackSegmentEvent('', { page: 'home' });
```

When calling `trackSegmentEvent` with a valid event name string, the function exits early and doesn't track anything. The validation logic appears to be inverted.

### Expected behavior
- Valid event names (non-empty strings) should be tracked successfully
- Empty strings or non-string values should be rejected and return early
- The analytics payload should be sent to `window.analytics.track` when a proper event name is provided

### System Info
- Insomnia version: latest
- Node version: 18.x

---
Repository: /testbed
