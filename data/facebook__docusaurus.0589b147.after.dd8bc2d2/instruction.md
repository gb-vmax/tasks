# Bug Report

### Describe the bug

I'm experiencing an issue with image syntax parsing in markdown. When using the `![` syntax to create images, the parser seems to be incorrectly handling certain characters, particularly the caret (`^`) character that follows the image syntax.

### Reproduction

```markdown
![alt text](image.url)^footnote
```

The parser appears to be rejecting valid image syntax or accepting invalid syntax depending on the presence of a `^` character immediately after the image closing bracket.

### Expected behavior

The image syntax should be parsed correctly regardless of what character follows the closing bracket `]`. The `^` character should be treated as a separate token and not affect the validity of the preceding image syntax.

### Additional context

This seems related to footnote support detection in the parser. The logic for determining when to accept or reject the image token appears to be inverted - it's doing the opposite of what it should be doing when checking for the caret character in combination with footnote support.

---
Repository: /testbed
