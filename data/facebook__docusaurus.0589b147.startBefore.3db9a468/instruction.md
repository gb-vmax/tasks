# Bug Report

### Describe the bug

I'm encountering an issue with fenced code block parsing in markdown. When processing markdown with code fences, the parser seems to be getting stuck or producing malformed output. The closing fence of code blocks is not being recognized properly.

### Reproduction

```js
const markdown = `
\`\`\`js
console.log('test');
\`\`\`
`;

// Parse the markdown
const result = remark().parse(markdown);
// The code fence doesn't close properly
```

### Expected behavior

Code fences should be parsed correctly with proper opening and closing. The parser should recognize the closing fence and properly exit the code block context.

### System Info
- remark version: 15.0.1
- Node version: 18.x

This seems to have started recently. The parser appears to be entering some state multiple times or not properly transitioning between states when handling the line endings around code fences.

---
Repository: /testbed
