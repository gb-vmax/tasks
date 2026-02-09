# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a closing fence has the exact same number of backticks (or tildes) as the opening fence, it's not being recognized as a valid closing fence anymore.

### Reproduction

```markdown
```js
console.log('test');
```
```

The above code block should close properly since both fences have 3 backticks, but it's not being recognized as closed. The parser seems to require the closing fence to have MORE characters than the opening fence, which is incorrect behavior.

Another example:
```markdown
~~~~python
def hello():
    print("world")
~~~~
```

With 4 tildes on both sides, this also fails to close properly.

### Expected behavior

According to the CommonMark spec, a closing code fence should have at least the same number of fence characters as the opening fence, not strictly more. A fence with exactly the same number of characters should be valid and close the code block.

### System Info
- Markdown parser: remark 15.0.1
- This appears to be a recent regression as it was working correctly before

---
Repository: /testbed
