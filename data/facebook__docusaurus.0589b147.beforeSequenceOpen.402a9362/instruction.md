# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When parsing code blocks, the initial prefix calculation seems to be incorrect, causing the parser to misidentify or incorrectly handle indented code fences.

### Reproduction

```js
const markdown = `
    \`\`\`js
    const x = 1;
    \`\`\`
`;

// Parse the markdown
const result = remark().parse(markdown);
// The code block is not correctly recognized or the prefix is calculated wrong
```

### Expected behavior

Fenced code blocks with leading whitespace/indentation should be parsed correctly. The parser should properly calculate the initial prefix length to determine the indentation level of the code fence.

### Additional context

This seems to affect code blocks that have indentation before the opening fence. The prefix calculation appears to be looking at the wrong event in the event stream, which causes it to use incorrect length values.

---
Repository: /testbed
