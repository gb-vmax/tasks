# Bug Report

### Describe the bug

Links in markdown are being parsed incorrectly - the closing parenthesis `)` is being treated as the opening parenthesis `(` in the resource tokenizer. This causes links with URLs to fail parsing or behave unexpectedly.

### Reproduction

```markdown
[example link](https://example.com)
```

When parsing this markdown, the link doesn't work correctly because the parser is checking for the wrong character code. It's looking for `(` (code 40) instead of `)` (code 41) when determining if the resource has ended.

### Expected behavior

The markdown link should be parsed correctly and the URL should be properly extracted. The closing parenthesis should close the link resource, not be treated as an opening parenthesis.

### Additional context

This appears to be affecting the `tokenizeResource` function in the remark parser. The character code comparison seems to be using the wrong value for detecting the end of a link resource.

---
Repository: /testbed
