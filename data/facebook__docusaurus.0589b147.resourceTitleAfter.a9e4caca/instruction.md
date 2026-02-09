# Bug Report

### Describe the bug

I'm encountering an issue with markdown link parsing where links with titles containing whitespace are not being parsed correctly. The parser seems to be handling the whitespace after the title improperly, causing the link syntax to break.

### Reproduction

```markdown
[link text](url "title with spaces")
```

When parsing this markdown, the link doesn't get recognized properly. It seems like the parser is not correctly consuming whitespace characters after the title portion of the link.

### Expected behavior

The parser should correctly handle links that have titles with spaces, and any whitespace between the title and the closing parenthesis should be properly consumed before finalizing the resource token.

Links like `[text](url "title")` with whitespace before the closing `)` should parse correctly, similar to how they work in standard markdown parsers.

### Additional context

This appears to be related to how the tokenizer processes characters after the title in resource definitions. The whitespace handling logic seems inverted - it's not properly factoring in the whitespace before moving to the end state.

---
Repository: /testbed
