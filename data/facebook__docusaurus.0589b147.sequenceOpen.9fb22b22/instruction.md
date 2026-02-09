# Bug Report

### Describe the bug

Fenced code blocks with exactly 3 backticks or tildes are not being recognized properly. The parser seems to reject valid markdown code blocks that should be accepted according to the CommonMark spec.

### Reproduction

```markdown
```js
console.log('hello');
```
```

When parsing the above markdown, the code block is not recognized as a valid fenced code block even though it uses the standard 3-backtick syntax.

### Expected behavior

Fenced code blocks with exactly 3 fence characters (backticks or tildes) should be properly parsed and recognized. According to the CommonMark specification, a code fence must begin with at least 3 consecutive backtick or tilde characters.

The following should all be valid:
- ` ``` ` (3 backticks)
- ` ~~~~ ` (4 tildes)
- ` ````` ` (5 backticks)

But currently it seems like only 4+ fence characters are being accepted.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
