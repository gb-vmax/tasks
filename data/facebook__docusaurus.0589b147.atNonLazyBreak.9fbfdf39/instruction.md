# Bug Report

### Describe the bug

I'm encountering an issue with fenced code block parsing in markdown. It seems like the closing fence of code blocks is not being recognized properly, causing the parser to treat the closing fence as part of the code content instead of as a delimiter.

### Reproduction

```markdown
\`\`\`js
console.log('test');
\`\`\`
```

When parsing this markdown, the closing fence (\`\`\`) is being included in the code block content rather than being treated as the end of the code block.

### Expected behavior

The parser should correctly identify the closing fence and end the code block there. The closing fence should not be part of the actual code content.

### Additional context

This appears to affect all fenced code blocks regardless of the language specified. The opening fence is detected correctly, but the closing logic seems broken.

---
Repository: /testbed
