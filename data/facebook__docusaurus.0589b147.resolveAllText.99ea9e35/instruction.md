# Bug Report

### Describe the bug
I'm experiencing an issue with markdown parsing where consecutive data events are not being merged correctly. The text content appears to be getting corrupted or lost when there are multiple adjacent data tokens.

### Reproduction
```js
// When parsing markdown with consecutive text data
const markdown = "some text here";
const result = parse(markdown);

// Expected: properly merged text content
// Actual: text appears to be missing or incorrectly merged
```

This seems to happen specifically when there are multiple consecutive "data" type events that should be merged together. The merging logic appears to be removing the wrong number of events from the array.

### Expected behavior
Consecutive data events should be properly merged into a single event with the correct start and end positions, and all intermediate events should be removed correctly.

### System Info
- remark version: 15.0.1
- Node version: latest

---
Repository: /testbed
