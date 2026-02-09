# Bug Report

### Describe the bug

I'm experiencing an issue with text parsing where the parser seems to be exiting the "data" state prematurely. This is causing unexpected behavior when processing markdown content with certain text patterns.

### Reproduction

```js
// When parsing text content that should continue in data state
const input = "Some regular text content";

// The parser exits the data state too early
// This affects how subsequent characters are processed
```

The issue appears to be related to how the data function handles code consumption and state transitions. Instead of staying in the data state while consuming characters, it's exiting prematurely.

### Expected behavior

The parser should remain in the "data" state while consuming regular text characters, only exiting when it encounters a break condition. The current behavior causes the parser to exit the data state before properly consuming all the text content.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like a regression as the parsing logic was working correctly before. The early exit is disrupting the normal flow of text processing.

---
Repository: /testbed
