# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a code fence has an info string but no metadata, the parser seems to be entering an incorrect state. The `codeFencedFenceMeta` token is being created even when there's no actual metadata present.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('hello');
\`\`\`
`;

// Parse the markdown
const result = parse(markdown);
```

When parsing a fenced code block with just a language identifier (like `javascript` above) and no additional metadata, the parser incorrectly attempts to process metadata that doesn't exist.

### Expected behavior

The parser should only enter the `codeFencedFenceMeta` state when there is actual metadata present after the info string. For a simple code fence like:

```
\`\`\`javascript
code here
\`\`\`
```

No metadata token should be created since there's no metadata after the language identifier.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
