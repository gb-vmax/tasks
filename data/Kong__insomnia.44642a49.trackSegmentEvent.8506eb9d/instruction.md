# Bug Report

### Describe the bug

After a recent update, the analytics tracking seems to have broken. When `trackSegmentEvent` is called, the event properties and context are being swapped in the call to `window.analytics.track()`.

### Reproduction

```js
// Call trackSegmentEvent with properties and context
global.main.trackSegmentEvent('Button Clicked', 
  { buttonId: 'submit', page: 'checkout' },
  { context: { userId: '123', sessionId: 'abc' } }
);

// Expected: window.analytics.track should receive:
// - event: 'Button Clicked'
// - properties: { buttonId: 'submit', page: 'checkout' }
// - options with context: { userId: '123', sessionId: 'abc' }

// Actual: properties and context are swapped
// The context object is passed as properties and vice versa
```

### Expected behavior

The `window.analytics.track()` method should be called with the correct parameter order:
1. Event name
2. Properties object (the actual event properties)
3. Options object containing the context

Currently it appears the properties and context are being passed in the wrong positions, which breaks analytics tracking.

### System Info
- Insomnia version: latest
- OS: All platforms affected

---
Repository: /testbed
