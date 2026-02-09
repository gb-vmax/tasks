# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link parsing where links with titles that have no whitespace after them are not being parsed correctly. The parser seems to be handling the whitespace check incorrectly, causing valid markdown links to fail parsing.

### Reproduction

```markdown
[link text](url "title")
```

When parsing markdown links with titles, the parser doesn't properly handle cases where there's no whitespace between the title and the closing parenthesis. This causes the link to either not be recognized or be parsed incorrectly.

Steps to reproduce:
1. Create a markdown string with a link that includes a title
2. Parse the markdown
3. The link may not be recognized or parsed as expected

### Expected behavior

Markdown links with titles should be parsed correctly regardless of whitespace positioning after the title. The parser should properly handle both cases:
- `[text](url "title" )` - with whitespace
- `[text](url "title")` - without whitespace

Both formats are valid markdown and should work identically.

### System Info
- remark version: 15.0.1

---
Repository: /testbed
