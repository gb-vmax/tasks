# Bug Report

### Describe the bug

Code fences with exactly 3 backticks or tildes are not being recognized properly. The parser seems to reject valid fenced code blocks that should be accepted according to the CommonMark spec.

### Reproduction

```markdown
```js
console.log('hello');
```
```

The above valid markdown with a 3-backtick code fence is not being parsed correctly. It appears the tokenizer is rejecting code blocks that use the minimum required fence length.

### Expected behavior

Code blocks with exactly 3 fence characters (backticks or tildes) should be recognized and parsed correctly, as this is the minimum valid fence length per the CommonMark specification.

### Additional context

This seems to affect the `tokenizeCodeFenced` function in the MDX parser. Both opening sequences with 3 characters and potentially longer sequences may be impacted.

---
Repository: /testbed
