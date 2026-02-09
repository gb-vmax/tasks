# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where the state restoration mechanism doesn't work correctly. When the parser backtracks or attempts to restore a previous state, the stack doesn't get properly reset to its original state, causing parsing errors or unexpected behavior.

### Reproduction

```js
// This happens when parsing markdown with complex nested structures
// that require the parser to backtrack and try alternative parsing strategies

const markdown = `
- List item with **bold
  and continuation
- Another item
`;

// The parser attempts to parse the bold syntax, fails, and tries to restore state
// But the stack state is not properly restored, leading to incorrect parsing
```

### Expected behavior

When the parser backtracks and restores a previous state, all internal state including the stack should be properly restored to the exact state it was in before. This ensures that alternative parsing strategies can be attempted cleanly without contamination from previous failed attempts.

### Additional context

This seems to affect parsing of complex markdown structures where the parser needs to try multiple interpretations of the same input. The issue appears to be related to how the internal stack is being saved and restored during tokenization.

---
Repository: /testbed
