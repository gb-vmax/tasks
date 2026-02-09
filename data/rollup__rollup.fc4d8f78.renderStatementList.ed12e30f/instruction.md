# Bug Report

### Describe the bug

I'm experiencing an issue with rendering statement lists where the output appears to be incorrectly formatted or missing statements. It seems like the first statement in a list isn't being processed correctly, which causes the generated code to be malformed.

### Reproduction

```js
// When bundling code with multiple statements
const input = `
  const a = 1;
  const b = 2;
  const c = 3;
`;

// The first statement (const a = 1;) is not rendered properly
// or boundaries are calculated incorrectly
```

### Expected behavior

All statements in the list should be rendered correctly with proper boundaries and line breaks. The first statement should be included in the output just like any other statement in the list.

### Additional context

This might be related to how statement boundaries are calculated when iterating through the statement list. The issue appears when there are multiple statements that need to be rendered together.

---
Repository: /testbed
