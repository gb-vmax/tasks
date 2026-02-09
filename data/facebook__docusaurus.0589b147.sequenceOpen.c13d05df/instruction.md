# Bug Report

### Describe the bug

Fenced code blocks with exactly 3 backticks or tildes are not being recognized properly. The parser seems to reject valid markdown code fences that should be accepted according to the CommonMark spec.

### Reproduction

```markdown
```js
console.log('hello');
```
```

When parsing the above markdown, the code block is not being recognized as a valid fenced code block, even though three backticks is the minimum required delimiter.

### Expected behavior

According to CommonMark specification, fenced code blocks should be opened with at least 3 consecutive backticks (or tildes). A code fence with exactly 3 delimiter characters should be valid and properly parsed.

The parser should accept:
- ` ``` ` (3 backticks)
- ` ```` ` (4 backticks)
- ` ````` ` (5 backticks)
- etc.

Currently it appears that only code fences with MORE than 3 delimiters are being accepted.

### Additional context

This affects any markdown content using the standard 3-backtick code fence syntax, which is the most common way to denote code blocks in markdown.

---
Repository: /testbed
