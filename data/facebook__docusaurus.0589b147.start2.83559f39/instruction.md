# Bug Report

### Describe the bug

I'm encountering an issue with markdown parsing where blank lines with leading whitespace are not being handled correctly. The parser seems to be rejecting valid blank lines that contain only whitespace characters before the line ending.

### Reproduction

```js
const markdown = `
Some content

    
More content
`;

// Parse the markdown
const result = parseMarkdown(markdown);
```

When parsing markdown with blank lines that have leading spaces or tabs, the parser fails to recognize them as valid blank lines. This causes unexpected parsing behavior where content that should be separated by blank lines gets treated incorrectly.

### Expected behavior

Blank lines with leading whitespace (spaces/tabs) should be treated as valid blank lines, just like completely empty lines. The markdown spec allows for blank lines to contain any amount of whitespace.

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
