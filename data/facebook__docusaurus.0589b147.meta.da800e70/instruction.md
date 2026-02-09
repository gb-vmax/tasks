# Bug Report

### Describe the bug

When using fenced code blocks in markdown with backticks in the info string (the part after the opening fence), the parser incorrectly rejects valid syntax. It seems like backticks that appear in the meta/info section are causing the parser to fail even when they shouldn't.

### Reproduction

```js
const markdown = `
\`\`\`javascript \`someAttribute\`
console.log('test');
\`\`\`
`;

// Parser fails to handle this correctly
```

The above code block should be valid - having backticks in the info string after the language identifier should be allowed, but the parser is rejecting it.

### Expected behavior

Fenced code blocks with backticks in the info/meta string should parse correctly. The backtick in the info string is different from the fence marker and shouldn't cause parsing to fail.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
