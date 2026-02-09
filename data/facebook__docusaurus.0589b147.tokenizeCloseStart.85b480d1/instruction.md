# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When I have a closing fence that's the same length as the opening fence, the code block doesn't close properly. It seems like the parser is requiring the closing fence to be *longer* than the opening fence instead of just equal length.

### Reproduction

```markdown
```js
const x = 1;
```
```

The above code block should be parsed correctly, but the closing fence with three backticks isn't being recognized. Only if I add extra backticks (like four or more) does it actually close the block.

### Expected behavior

According to the CommonMark spec, a closing code fence should close the block if it has at least as many backticks as the opening fence. So three backticks should close a block opened with three backticks.

Currently it seems like the closing fence needs to have MORE backticks than the opening fence, which is incorrect behavior.

### Additional context

This appears to be affecting all fenced code blocks in my documents. Also noticing some weird behavior where spaces before the closing fence seem to affect whether it's recognized or not - sometimes it works with spaces, sometimes it doesn't.

---
Repository: /testbed
