# Bug Report

### Describe the bug

I'm experiencing an issue with the tokenizer's restore functionality. When the restore function is called, the events array doesn't get properly reset to its original state. The array appears to be cleared completely instead of being truncated to the correct starting index.

### Reproduction

```js
const context = {
  events: [/* some initial events */],
  // ... other context properties
};

// After tokenization starts
const startEventsIndex = context.events.length; // e.g., 5

// More events are added during tokenization
context.events.push(event1, event2, event3); // now length is 8

// When restore() is called
restore(); 

// Expected: context.events.length should be 5 (startEventsIndex)
// Actual: context.events.length is 0 (all events removed)
```

### Expected behavior

The `restore()` function should truncate the events array back to `startEventsIndex`, preserving the events that existed before the tokenization attempt started. Instead, it appears to be removing all events from the beginning of the array.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This is causing parsing to fail in certain edge cases where the tokenizer needs to backtrack and restore its previous state.

---
Repository: /testbed
