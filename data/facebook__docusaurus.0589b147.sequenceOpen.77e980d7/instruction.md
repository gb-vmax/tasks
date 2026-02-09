# Bug Report

### Describe the bug

I'm experiencing issues with fenced code blocks in markdown parsing. It seems like the parser is rejecting valid code blocks that should be accepted, and in some cases may be accepting invalid ones.

### Reproduction

```markdown
```js
console.log('test');
```
```

When trying to parse markdown with standard fenced code blocks (using three backticks), the parser doesn't recognize them properly. The code blocks that should be valid are being rejected.

### Expected behavior

Standard fenced code blocks with exactly 3 backticks (```) should be parsed correctly and recognized as valid code fence sequences. The parser should accept these common markdown patterns.

### Additional context

This appears to have started recently. The logic for determining valid fence sequences seems off - it's treating valid 3-character fence sequences as invalid. Also noticed some strange behavior with how whitespace after the fence is being handled.

---
Repository: /testbed
