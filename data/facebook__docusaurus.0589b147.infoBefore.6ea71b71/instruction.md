# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When parsing code blocks with info strings (language identifiers), the parser seems to be handling them incorrectly in certain contexts, particularly when dealing with interrupts.

### Reproduction

```js
const markdown = `
Some text

\`\`\`javascript
const x = 1;
\`\`\`

More text
`;

// Parse the markdown
const result = parse(markdown);
```

The code block should be properly recognized and parsed with its info string, but the behavior appears inconsistent depending on whether the code block interrupts other content or not.

### Expected behavior

Fenced code blocks with language identifiers should be consistently parsed regardless of the context they appear in. The info string (e.g., "javascript") should be properly captured and the code fence should be correctly identified.

### Additional context

This seems to affect how code blocks are tokenized when they appear in different positions within the document. The issue might be related to how the parser determines whether a code block is interrupting other content.

---
Repository: /testbed
