# Bug Report

### Describe the bug

Fenced code blocks with closing fence sequences that are exactly the same length as the opening fence are not being recognized properly. The parser seems to require the closing fence to be strictly longer than the opening fence, which breaks standard markdown behavior.

### Reproduction

```markdown
```js
console.log('test');
```
```

When parsing this markdown, the closing fence (three backticks) should properly close the code block that was opened with three backticks. However, the parser doesn't recognize it as a valid closing fence.

This also affects other fence lengths:
```markdown
````
code here
````
```

The four-backtick closing fence should close the four-backtick opening fence, but it doesn't work as expected.

### Expected behavior

According to the CommonMark spec, a closing code fence should be recognized when it has **at least** as many backticks (or tildes) as the opening fence, not strictly more. A fence with the same number of characters should successfully close the code block.

### System Info
- Using remark@15.0.1
- This appears to be a regression as it worked correctly in earlier versions

---
Repository: /testbed
