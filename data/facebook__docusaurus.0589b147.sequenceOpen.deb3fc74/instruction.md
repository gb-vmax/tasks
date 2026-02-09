# Bug Report

### Describe the bug

Fenced code blocks with exactly 3 backticks or tildes are not being recognized properly. When trying to create a code block with the standard 3-character fence syntax, the parser fails to treat it as a valid code fence.

### Reproduction

```markdown
```javascript
console.log('hello');
```
```

The above code block with exactly 3 backticks should be parsed as a valid fenced code block, but it's not being recognized.

This also affects tilde-based fences:

```markdown
~~~python
print('hello')
~~~
```

### Expected behavior

According to the CommonMark specification, fenced code blocks should be recognized with a minimum of 3 consecutive backticks or tildes. The parser should accept exactly 3 characters as a valid fence opening sequence.

Currently it seems like only 4 or more characters are being accepted as valid fence markers, which breaks compatibility with standard markdown syntax.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
