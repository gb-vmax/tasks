# Bug Report

### Describe the bug

I'm encountering an issue with MDX link parsing where links followed by a caret character (`^`) are not being parsed correctly. The parser seems to be rejecting valid link syntax when a caret appears immediately after the closing bracket.

### Reproduction

```markdown
[link text](url)^some text
```

When parsing the above MDX content, the link is not recognized as valid and fails to parse properly. This appears to be related to how the label tokenizer handles characters following link syntax.

### Expected behavior

Links followed by a caret character should be parsed normally. The caret is a valid character that can appear in regular text after a link, and shouldn't affect link parsing.

For example:
```markdown
[my link](https://example.com)^1
```

Should render the link correctly with "^1" appearing as regular text after it.

### System Info
- MDX version: 3.0.0
- Parser: micromark-based tokenizer

This seems to have started happening recently. Links work fine when followed by other characters, just not with carets.

---
Repository: /testbed
