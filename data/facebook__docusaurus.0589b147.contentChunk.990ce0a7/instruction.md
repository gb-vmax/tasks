# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When processing code blocks, empty lines within the code block are not being handled correctly, causing the parser to behave unexpectedly.

### Reproduction

```js
const markdown = `
\`\`\`js
function test() {
  console.log('hello');

  console.log('world');
}
\`\`\`
`;

// Parse the markdown
const result = parse(markdown);
```

When the code block contains empty lines (like the blank line between the two console.log statements), the parsing doesn't work as expected. The code block content seems to be truncated or incorrectly tokenized.

### Expected behavior

Empty lines within fenced code blocks should be preserved and parsed correctly as part of the code content. The entire code block should be treated as a single unit regardless of internal blank lines.

### Additional context

This seems to affect the `tokenizeCodeFenced` function specifically when processing the content chunks of code blocks. The issue appears when there are line endings within the code block content.

---
Repository: /testbed
