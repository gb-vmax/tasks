# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a closing fence has exactly the same number of backticks (or tildes) as the opening fence, the code block doesn't close properly. It seems like the parser is requiring MORE characters in the closing fence than the opening fence, rather than the same number or more.

### Reproduction

```markdown
```js
console.log('test')
```
```

The above code block with three backticks opening and three backticks closing doesn't parse correctly. The closing fence isn't recognized.

However, this works:

```markdown
```js
console.log('test')
````
```

Using four backticks to close a three-backtick opening fence works, but that's not the expected behavior according to CommonMark spec.

### Expected behavior

According to CommonMark specification, a closing code fence should have at least the same number of backticks/tildes as the opening fence. So three backticks should be able to close a block opened with three backticks.

The parser should recognize:
- 3 backticks closing a 3 backtick block ✓
- 4 backticks closing a 3 backtick block ✓
- 2 backticks closing a 3 backtick block ✗

Currently it seems like only the second case works.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
