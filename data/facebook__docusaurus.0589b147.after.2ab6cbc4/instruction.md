# Bug Report

### Describe the bug

I'm encountering an issue with image syntax parsing in MDX. When trying to use images with the `^` character immediately following the opening bracket (like `![^text]`), the parser is not handling them correctly. It seems like the logic for detecting footnote support is inverted.

### Reproduction

```markdown
![^example](image.png)
```

When parsing this MDX content, the image syntax is not being recognized properly. The parser appears to be rejecting valid image syntax when it encounters a `^` character after the opening bracket.

### Expected behavior

The parser should correctly handle image syntax even when the text starts with `^`. The image should be parsed as a normal image reference, not confused with footnote syntax.

### Additional context

This seems related to the footnote support detection logic in the label tokenizer. The behavior changed recently and is now preventing legitimate image syntax from being parsed correctly.

---
Repository: /testbed
