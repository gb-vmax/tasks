# Bug Report

### Describe the bug
When parsing markdown links with resources (e.g., `[text](url)`), the parser seems to hang or behave unexpectedly. Links that should be properly parsed are not being recognized correctly.

### Reproduction
```markdown
[Example Link](https://example.com)
```

When trying to parse the above markdown, the link is not being processed as expected. The parser appears to get stuck or fails to properly tokenize the resource part of the link.

### Expected behavior
The markdown link should be parsed correctly and the resource (URL) should be properly tokenized. The parser should complete without hanging.

### Additional context
This seems to affect all markdown links with resources. Simple text links work fine, but as soon as you add a URL in parentheses, the parsing breaks down.

---
Repository: /testbed
