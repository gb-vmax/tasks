# Bug Report

### Describe the bug

Markdown links with titles are not being parsed correctly. When I try to use a link with a title attribute (like `[text](url "title")`), the parser seems to completely ignore the title or fails to recognize it.

### Reproduction

```markdown
[Example](https://example.com "This is a title")
```

The title part `"This is a title"` is not being processed as expected. It seems like the parser is not detecting the quote characters that start the title section.

### Expected behavior

The parser should correctly recognize and process link titles enclosed in double quotes, single quotes, or parentheses, as per the CommonMark specification. All three of these should work:

```markdown
[link](url "double quotes")
[link](url 'single quotes')
[link](url (parentheses))
```

Currently none of these title formats seem to be working properly.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
