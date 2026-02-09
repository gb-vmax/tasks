# Bug Report

### Describe the bug

Fenced code blocks with exactly 3 backticks or tildes are not being recognized properly. The parser seems to be rejecting valid markdown code fences.

### Reproduction

```markdown
```js
console.log('hello');
```
```

When parsing the above markdown, the code block is not being tokenized correctly. The same issue occurs with tildes:

```markdown
~~~
some code
~~~
```

Both of these should be valid fenced code blocks according to the CommonMark spec, but they're being treated as regular text instead.

### Expected behavior

Code blocks with exactly 3 fence characters (backticks or tildes) should be properly recognized and parsed as fenced code blocks. The parser should accept 3 or more fence characters, not require more than 3.

### Additional context

This appears to affect the basic use case for fenced code blocks. Most markdown documents use the standard 3-character fence syntax, so this is breaking a lot of previously working content.

---
Repository: /testbed
