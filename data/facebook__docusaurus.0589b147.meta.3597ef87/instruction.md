# Bug Report

### Describe the bug
When using fenced code blocks with backticks in markdown, the parser is not handling the info string correctly. It seems like the parser is accepting backticks in the metadata section when it shouldn't, causing parsing issues with code blocks.

### Reproduction
```markdown
```javascript`test
console.log('hello');
```
```

The above code block with a backtick in the info string should be rejected but instead gets processed incorrectly.

### Expected behavior
Fenced code blocks should reject backticks in the info/meta string section. The parser should fail when encountering a backtick character after the opening fence and language identifier.

For example, this should not be valid:
- ` ```js`metadata ` (backtick in meta)
- ` ```~~~mixed ` (when using tildes as fence marker)

The parser should properly validate that backticks don't appear in the metadata portion of fenced code blocks.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
