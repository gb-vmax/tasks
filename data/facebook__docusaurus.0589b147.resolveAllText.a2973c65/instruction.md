# Bug Report

### Describe the bug

I'm experiencing an issue with text merging in the remark parser. When processing consecutive "data" type events, the merging logic seems to be removing the wrong elements from the events array, causing text content to be lost or incorrectly positioned.

### Reproduction

```js
// When parsing markdown with consecutive data events
const events = [
  ['enter', { type: 'data', value: 'Hello' }],
  ['exit', { type: 'data' }],
  ['enter', { type: 'data', value: ' ' }],
  ['exit', { type: 'data' }],
  ['enter', { type: 'data', value: 'World' }],
  ['exit', { type: 'data' }]
];

// After processing through resolveAllText
// Expected: Events should be merged correctly with proper boundaries
// Actual: Some data events are incorrectly removed or boundaries are wrong
```

### Expected behavior

Consecutive data events should be properly merged, preserving all text content and maintaining correct start/end boundaries. The splice operation should remove the correct range of events when merging.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have broken text parsing in certain edge cases where multiple adjacent text nodes need to be combined. The issue appears to be related to how the events array is being modified during the merge process.

---
Repository: /testbed
