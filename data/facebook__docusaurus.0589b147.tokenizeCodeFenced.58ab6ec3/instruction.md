# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. Code blocks with exactly 3 backticks or tildes are being rejected, and the content indentation inside code blocks appears to be handled incorrectly.

### Reproduction

```markdown
```javascript
console.log('hello');
```
```

When trying to parse a standard fenced code block with exactly 3 fence characters (backticks or tildes), it's not being recognized properly. Additionally, code blocks with specific indentation patterns seem to have their content shifted incorrectly.

### Expected behavior

- Fenced code blocks with exactly 3 fence characters should be valid and parse correctly (this is the standard markdown syntax)
- Content indentation within code blocks should be preserved accurately based on the opening fence's indentation

### System Info
- remark version: 15.0.1

This seems like a regression as standard markdown code blocks are a fundamental feature. Any code block using the minimal 3-character fence is affected.

---
Repository: /testbed
