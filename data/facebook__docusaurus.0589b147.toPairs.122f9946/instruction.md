# Bug Report

### Describe the bug

I'm encountering an issue with find-and-replace functionality when passing in tuples. It seems like the first tuple in a list is being skipped during processing, which causes replacements to not work as expected.

### Reproduction

```js
const findAndReplace = require('remark-gfm');

// When passing a list of tuples like this:
const tuples = [
  [/pattern1/, 'replacement1'],
  [/pattern2/, 'replacement2']
];

// Only the second pattern gets processed
// The first pattern is completely ignored
```

When I provide multiple find-and-replace patterns, the first one in the list doesn't get applied. The text that should match the first pattern remains unchanged, while subsequent patterns work correctly.

### Expected behavior

All tuples in the list should be processed and applied. Each pattern should perform its replacement regardless of position in the array.

### System Info
- remark-gfm version: 4.0.0
- Node version: Latest

---
Repository: /testbed
