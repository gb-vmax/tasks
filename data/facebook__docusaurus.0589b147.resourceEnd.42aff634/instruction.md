# Bug Report

### Describe the bug

Links in markdown are not being parsed correctly. When I try to use standard markdown link syntax with a URL and title, the parser fails to recognize the closing parenthesis and the link doesn't render properly.

### Reproduction

```markdown
[Example Link](https://example.com "Title")
```

The link should be parsed as a valid markdown link, but instead it's being treated as plain text or malformed syntax.

I've also tried simpler cases:

```markdown
[Simple Link](https://example.com)
```

These also don't seem to work as expected after the recent update.

### Expected behavior

The markdown parser should correctly recognize and parse link syntax with the resource (URL) enclosed in parentheses. The closing `)` should properly terminate the link resource section and the entire link should be converted to the appropriate HTML output.

### Additional context

This seems to have started happening recently. Links were working fine before, but now they're not being processed correctly. The issue appears to be related to how the parser handles the closing parenthesis of link resources.

---
Repository: /testbed
