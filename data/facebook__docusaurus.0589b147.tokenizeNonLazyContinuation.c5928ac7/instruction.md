# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where content after code blocks is being incorrectly handled. It seems like the parser is treating subsequent paragraphs as part of the code block or not parsing them at all when they should be treated as separate content.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');
\`\`\`

This paragraph should be parsed separately but isn't showing up correctly.
`;

// Parse the markdown
const result = remark.parse(markdown);
// The paragraph after the code block is missing or malformed in the AST
```

### Expected behavior

Content following a code block should be parsed as a separate paragraph node in the AST. The parser should correctly identify where the code block ends and regular content begins.

### Additional context

This seems to affect any content that comes after fenced code blocks. The issue appears to be related to how the parser handles line continuations after code blocks - it's either including content that shouldn't be part of the block or excluding content that should be parsed separately.

---
Repository: /testbed
