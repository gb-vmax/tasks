# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a closing fence has the same number of backticks as the opening fence, it's not being recognized as a valid closing delimiter.

### Reproduction

```markdown
```js
const x = 1;
```
```

The above code block with three backticks opening and three backticks closing is not being parsed correctly. The closing fence should be recognized, but it appears to be ignored.

### Expected behavior

A fenced code block should close properly when the closing fence has the same number of characters (backticks or tildes) as the opening fence. According to the CommonMark spec, the closing fence must have at least as many characters as the opening fence.

For example:
- Opening with ``` should close with ``` or more
- Opening with ```` should close with ```` or more

Currently it seems like the closing fence needs to have MORE characters than the opening fence, which is incorrect behavior.

### Additional context

This affects any fenced code blocks where the opening and closing delimiters have exactly the same length. It's breaking basic markdown rendering for standard code blocks.

---
Repository: /testbed
