# Bug Report

### Describe the bug

I'm encountering an issue with MDX image syntax parsing where images followed by a caret character (`^`) are not being recognized correctly. It seems like the parser is rejecting valid image syntax when there's a `^` character immediately after the closing bracket.

### Reproduction

```markdown
![alt text](image.png)^
```

When I try to parse this MDX content, the image syntax is not being processed as expected. The parser appears to be treating the `^` character as something that invalidates the entire image syntax, even though it should just be regular text following the image.

### Expected behavior

The image should be parsed normally and the `^` character should be treated as plain text that follows the image. The presence of a caret after an image shouldn't affect the image parsing itself.

### Additional context

This seems to be related to how the label tokenizer handles characters that come after image syntax. The issue only manifests when there's a `^` character immediately following the image closing bracket - other characters work fine.

---
Repository: /testbed
