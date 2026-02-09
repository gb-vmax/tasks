# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where line breaks in text data are being consumed incorrectly. When the parser encounters a break character, it seems to be consuming it twice - once when exiting the "data" state and again when transitioning to the next state.

### Reproduction

```js
const text = "Some text\nwith a line break";
const result = parseMarkdown(text);
// The line break character appears to be consumed/processed incorrectly
```

When parsing text that contains line breaks or other break characters, the parser doesn't handle them properly. The break character gets consumed during state transition, which leads to unexpected parsing behavior.

### Expected behavior

Line breaks and other break characters should be processed correctly during state transitions. The parser should only consume the break character once, not multiple times during the transition from the "data" state.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
