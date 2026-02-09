# Bug Report

### Describe the bug

I'm encountering an issue with fenced code blocks in markdown parsing. When a code fence closing sequence (like ` ``` `) is followed by end-of-file (EOF) without a newline, the parser doesn't properly close the code block. The fence should be recognized and closed even when there's no trailing newline character.

### Reproduction

```js
const markdown = '```js\nconst x = 1;\n```';  // Note: no newline after closing fence

// Parse this markdown
// Expected: code block should be properly closed
// Actual: code block is not recognized as closed
```

Another example:
```
```python
print("hello")
```
```
(where the last line has no newline character at EOF)

### Expected behavior

The closing fence should be recognized and the code block should be properly terminated even when the closing fence is at EOF without a trailing newline. This is valid markdown syntax and should be handled correctly.

### System Info
- remark version: 15.0.1

This seems to have started happening recently. The parser should handle EOF after a closing fence sequence just like it handles a newline.

---
Repository: /testbed
