# Bug Report

### Describe the bug

I'm experiencing an issue with directive parsing where colons (`:`) in certain contexts are not being handled correctly. It seems like the parser is checking the wrong event in the events array when determining if a colon should be treated as part of a directive or as a regular character.

### Reproduction

```js
// Example directive text that triggers the issue
const markdown = `
:directive[text with escaped \\: colon]
`

// The parser incorrectly processes the escaped colon
// Expected: The escaped colon should be treated as a literal character
// Actual: The directive parsing breaks or behaves unexpectedly
```

### Expected behavior

When a colon is escaped with a backslash (`\:`), it should be treated as a literal colon character and not interfere with directive syntax parsing. The parser should correctly identify character escapes by checking the appropriate event in the event history.

### Additional context

This appears to be related to how the parser validates whether a colon character is part of a directive syntax or should be treated as a regular character. The validation logic seems to be looking at the wrong position in the events array.

---
Repository: /testbed
