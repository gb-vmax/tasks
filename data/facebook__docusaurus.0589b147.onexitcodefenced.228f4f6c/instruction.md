# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks where leading newlines are not being stripped correctly. After some recent changes, code blocks now retain their leading newlines when they should be removed.

### Reproduction

```js
const markdown = `
\`\`\`javascript
console.log('test');
\`\`\`
`;

// Parse the markdown
const result = remark.parse(markdown);

// The code block value still contains the leading newline
console.log(result.children[0].value);
// Expected: "console.log('test');"
// Actual: "\nconsole.log('test');"
```

### Expected behavior

Both leading and trailing newlines should be stripped from fenced code blocks. The regex pattern should match newlines at the beginning OR end of the code content, not just at the end twice.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
