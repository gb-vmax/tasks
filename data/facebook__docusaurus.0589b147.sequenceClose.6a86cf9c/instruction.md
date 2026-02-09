# Bug Report

### Describe the bug
When using fenced code blocks in markdown, the closing fence is not being recognized correctly when it has the same number of backticks/tildes as the opening fence. The parser seems to require the closing fence to have MORE characters than the opening fence, which doesn't match the CommonMark specification.

### Reproduction
```markdown
```js
console.log('test');
```
```

The above code block should be properly closed, but it appears the closing fence with 3 backticks is not being recognized when the opening fence also has 3 backticks.

Another example:
```markdown
~~~~
some code
~~~~
```

The closing fence with 4 tildes should close a code block that was opened with 4 tildes, but this doesn't seem to work correctly.

### Expected behavior
According to CommonMark spec, a closing code fence should be recognized when it has **at least** as many backticks/tildes as the opening fence. A fence with exactly the same number of characters should properly close the code block.

### System Info
- remark version: 15.0.1
- Browser: N/A (server-side parsing)

---
Repository: /testbed
