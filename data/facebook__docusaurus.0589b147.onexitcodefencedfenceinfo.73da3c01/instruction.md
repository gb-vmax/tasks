# Bug Report

### Describe the bug
When parsing fenced code blocks in markdown, the language identifier is being extracted incorrectly. The `lang` property on code fence nodes contains an extra character at the beginning and seems to be accessing the wrong node in the stack.

### Reproduction
```js
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// Parse the markdown
const ast = parseMarkdown(markdown);

// The code block's lang property is incorrect
// Expected: 'javascript'
// Actual: 'avascript' (or similar - first character missing and wrong value)
```

### Expected behavior
The `lang` property should correctly contain the full language identifier specified after the opening code fence (e.g., `javascript`, `python`, `typescript`). The parser should extract the complete language string without any modifications or truncation.

### Additional context
This appears to affect all fenced code blocks with language identifiers. The issue seems related to how the parser handles the fence info during AST construction.

---
Repository: /testbed
