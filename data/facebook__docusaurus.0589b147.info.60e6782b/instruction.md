# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When using backticks (```) as the fence marker, the parser seems to be rejecting valid code blocks or not handling the fence info string correctly.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('hello');
\`\`\`
`;

// Parse the markdown
const result = remark.parse(markdown);
// The code block is not being recognized properly
```

Also happens with language identifiers:

```markdown
\`\`\`js
const x = 1;
\`\`\`
```

The code fence should be parsed correctly but it seems like the fence marker validation is failing.

### Expected behavior

Fenced code blocks with backticks should be parsed correctly and the language identifier (info string) should be properly extracted. The parser should recognize valid fence markers and process the code block content.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
