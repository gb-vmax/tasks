# Bug Report

### Describe the bug

I'm encountering an issue with strikethrough syntax in GFM (GitHub Flavored Markdown) parsing. When using consecutive tilde characters (`~`), the strikethrough is not being recognized correctly in certain cases.

### Reproduction

```markdown
This is ~~strikethrough~~ text.
```

The parser seems to be incorrectly handling the opening `~~` sequence. When I try to parse markdown with strikethrough, it's either not being detected at all or producing unexpected results with the token stream.

### Expected behavior

The strikethrough delimiters should be properly recognized and the text between `~~` should be marked as strikethrough. The parser should correctly identify valid strikethrough sequences and process them according to GFM spec.

### Additional context

This appears to be related to how the parser checks for valid strikethrough start sequences. The issue manifests when trying to use standard strikethrough syntax that should work according to GitHub Flavored Markdown specification.

---
Repository: /testbed
