# Bug Report

### Describe the bug

I'm experiencing an issue where statement lists are being rendered incorrectly, causing the first statement to be skipped or processed improperly. This seems to affect how code boundaries are determined during the rendering phase.

### Reproduction

When rendering a list of statements, the first statement in the list doesn't get processed correctly. This leads to incorrect output where the initial statement is either missing or has improper boundaries.

Example scenario:
```js
// Given a list of statements to render
const statements = [
  statementA,
  statementB,
  statementC
];

// The rendering process skips or mishandles statementA
// Only statementB and statementC are processed correctly
```

### Expected behavior

All statements in the list should be rendered correctly, including the first one. The boundary detection should work properly for every statement regardless of its position in the list.

### Additional context

This appears to be related to how the loop iterates through the statement list and how node boundaries are being checked. The issue manifests when dealing with statements that need boundary markers or have specific inclusion requirements.

---
Repository: /testbed
