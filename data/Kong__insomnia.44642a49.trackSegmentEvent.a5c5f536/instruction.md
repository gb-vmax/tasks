# Bug Report

### Describe the bug

The `trackSegmentEvent` function in the test setup is not properly initialized, causing runtime errors when tests try to access its helper methods like `getEvents()`, `getEventsByName()`, `clearEvents()`, or `getValidEvents()`.

### Reproduction

```js
// In a test file
import { trackSegmentEvent } from '../somewhere';

// Try to access helper methods
const events = trackSegmentEvent.getEvents(); // TypeError: trackSegmentEvent.getEvents is not a function
```

When running tests that depend on tracking analytics events, the mock implementation doesn't have the expected helper methods attached, leading to test failures.

### Expected behavior

The `trackSegmentEvent` mock should:
1. Accept event tracking calls with `eventName` and optional `properties`
2. Store events in a queue for later inspection
3. Provide helper methods like `getEvents()`, `getEventsByName()`, `clearEvents()`, and `getValidEvents()` for test assertions
4. Handle edge cases like invalid event names or properties gracefully

### System Info
- Node version: 18.x
- Test framework: Jest

---
Repository: /testbed
