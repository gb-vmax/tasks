# Bug Report

### Describe the bug

I'm experiencing an issue with fenced code blocks in markdown parsing. When a closing fence has the same number of backticks/tildes as the opening fence, it's not being recognized as a valid closing fence anymore.

### Reproduction

```markdown
```js
const x = 1;
```
```

The code block above should be properly closed, but the closing fence with exactly 3 backticks (matching the opening) is not being detected. It seems like the parser now requires the closing fence to have MORE characters than the opening fence instead of the same number or more.

### Expected behavior

According to the CommonMark spec, a closing code fence should be valid if it has at least the same number of fence characters as the opening fence. So if I open with 3 backticks, closing with 3 backticks should work.

For example:
- Opening with ``` (3 backticks) should close with ``` (3) or ```` (4+)
- Opening with ```` (4 backticks) should close with ```` (4) or ````` (5+)

Currently it seems like only strictly greater counts are accepted, which breaks standard markdown code blocks.

### Additional context

This affects basic markdown code blocks that most users write. The most common pattern of using exactly 3 backticks to open and close a code block no longer works correctly.

---
Repository: /testbed
