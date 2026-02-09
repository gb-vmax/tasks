# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where spaces are being handled incorrectly. It appears that the space detection logic has been inverted, causing the parser to enter a space token when it encounters non-space characters instead of actual spaces.

### Reproduction

```js
// Parse markdown with spaces
const markdown = `
Hello world

This is a test
`;

// The parser now treats non-space characters as spaces
// and actual spaces are not being recognized properly
```

When parsing markdown content that contains regular spaces (like between words or at the start of lines), the behavior is now reversed - the parser is treating non-space characters as if they were spaces and ignoring actual space characters.

### Expected behavior

The parser should correctly identify space characters (spaces, tabs, etc.) and handle them appropriately. Space characters should trigger the space handling logic, not non-space characters.

### System Info
- remark-gfm version: 4.0.0

This seems to have broken basic markdown parsing functionality. Any markdown with spaces between words or indentation is now being parsed incorrectly.

---
Repository: /testbed
