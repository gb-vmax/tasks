# Bug Report

### Describe the bug

Strikethrough markdown syntax is not rendering correctly. When I use double tildes (`~~text~~`) to create strikethrough text, it's not being parsed properly and the tildes are showing up in the output instead of creating the strikethrough effect.

### Reproduction

```markdown
This is ~~strikethrough text~~ in a sentence.
```

Expected output: This is ~~strikethrough text~~ in a sentence.
Actual output: The tildes are visible and the text is not struck through.

This seems to have broken recently - strikethrough was working fine before. I'm using the standard GFM (GitHub Flavored Markdown) syntax with double tildes.

### Expected behavior

Double tildes should properly mark text as strikethrough and render with a line through the text, following the GitHub Flavored Markdown specification.

---
Repository: /testbed
