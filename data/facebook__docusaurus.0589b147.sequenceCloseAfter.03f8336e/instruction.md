# Bug Report

### Describe the bug
Fenced code blocks in markdown are not being parsed correctly when there's content immediately after the closing fence. The parser seems to be accepting invalid syntax where characters appear right after the closing backticks without a line break.

### Reproduction
```markdown
\`\`\`javascript
console.log('test');
\`\`\`invalid
```

The above should fail to parse as a valid fenced code block since `invalid` appears immediately after the closing fence without a newline, but it's being accepted as valid markdown.

### Expected behavior
According to the CommonMark spec, fenced code blocks should only be closed by a fence (backticks or tildes) followed by optional spaces and then a line ending or end of file. Any other characters after the closing fence should invalidate it.

The parser should reject code blocks where the closing fence is followed by non-whitespace characters on the same line.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
