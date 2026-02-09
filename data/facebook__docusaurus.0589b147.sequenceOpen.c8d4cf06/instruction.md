# Bug Report

### Describe the bug

Code fences with exactly 3 backticks or tildes are not being recognized as valid fenced code blocks. The parser seems to be rejecting valid markdown syntax for code blocks.

### Reproduction

```markdown
```js
console.log('hello');
```
```

The above valid markdown code fence is not being parsed correctly. Code blocks with 3 fence characters should be valid according to the CommonMark spec, but they're being treated as invalid.

### Expected behavior

Fenced code blocks with exactly 3 backticks (or tildes) should be properly recognized and parsed. This is the minimum required fence length according to the markdown specification.

Example that should work:
```markdown
```
code here
```
```

### Additional context

This affects all code blocks using the minimum fence length of 3 characters. Code blocks with 4 or more fence characters seem to work fine, but the standard 3-character fence is broken.

---
Repository: /testbed
