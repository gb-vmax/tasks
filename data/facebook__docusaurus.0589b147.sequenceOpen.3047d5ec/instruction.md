# Bug Report

### Describe the bug

I'm encountering an issue with parsing fenced code blocks in markdown. It appears that code blocks with exactly 3 backticks or tildes are not being recognized correctly.

### Reproduction

```markdown
```js
console.log('hello');
```
```

When parsing the above markdown, the code block is not being detected as a valid fenced code block. The parser seems to be rejecting code fences that use exactly 3 fence characters.

### Expected behavior

According to the CommonMark spec, fenced code blocks should be valid when using 3 or more consecutive backticks (or tildes). A fence with exactly 3 characters should be recognized and parsed correctly.

The following should all be valid:
- ` ``` ` (3 backticks)
- ` ```` ` (4 backticks)
- `~~~` (3 tildes)
- `~~~~` (4 tildes)

Currently only fences with 4+ characters seem to work, while 3-character fences are being rejected.

### Additional context

This seems to have started happening recently. I'm using the remark parser and standard markdown code blocks are no longer working as expected.

---
Repository: /testbed
