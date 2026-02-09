# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where line endings are not being detected correctly. It seems like certain markdown content is being parsed incorrectly, particularly when dealing with line breaks and newlines.

### Reproduction

```js
// When parsing markdown with specific line ending characters
const markdown = `
Some text here
Another line
`;

// The parser fails to recognize proper line endings
// This causes the content to be treated as a single line instead of multiple lines
```

### Expected behavior

The parser should correctly identify markdown line endings (newlines, carriage returns, etc.) and process them appropriately. Multi-line content should be parsed as separate lines, not concatenated together.

### Additional context

This appears to affect how the markdown processor handles line breaks in the content. The logic for detecting line endings seems to have an issue with the condition checking.

---
Repository: /testbed
