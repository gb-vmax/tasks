# Bug Report

### Describe the bug

I'm encountering an issue with fenced code block parsing in markdown. When a fenced code block has an info string (language identifier) but no meta string, the parser seems to be handling it incorrectly. The behavior has changed and now empty meta sections are being processed differently than before.

### Reproduction

```markdown
```javascript
const x = 1;
```
```

When parsing the above code block, the meta handling logic appears to be inverted. Code blocks with just a language identifier (no additional meta information) are not being processed as expected.

### Expected behavior

Fenced code blocks with only an info string (like `javascript`, `python`, etc.) and no meta string should parse correctly without attempting to enter meta processing. The parser should only enter the meta state when there's actually meta content to process.

### System Info
- remark version: 15.0.1

This seems to have broken after a recent change to the tokenizer logic. The condition check for when to enter meta processing appears to be backwards now.

---
Repository: /testbed
