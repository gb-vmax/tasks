# Bug Report

### Describe the bug

When generating code frames for error messages, tabs in the source code are not being converted to spaces correctly. This results in misaligned code frames where the caret/arrow indicators don't point to the correct column position.

### Reproduction

```js
// Source code with tabs at the beginning
const code = '\t\tconst x = 5;';

// When an error occurs at a specific position, the code frame
// shows incorrect alignment because tabs aren't properly converted
```

For example, if you have source code that uses tabs for indentation and an error occurs, the visual indicator in the error message will be misaligned, making it difficult to identify where the actual error is in the code.

### Expected behavior

Tabs should be consistently converted to spaces throughout the entire line (not just leading tabs), and the code frame should properly align with the actual error position in the source code.

### System Info
- Rollup version: latest
- Node version: 18.x

---
Repository: /testbed
