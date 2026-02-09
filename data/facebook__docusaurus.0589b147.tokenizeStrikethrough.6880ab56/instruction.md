# Bug Report

### Describe the bug

Strikethrough formatting in GFM (GitHub Flavored Markdown) is not rendering correctly. When using the `~~` syntax for strikethrough text, the formatting appears to be applied incorrectly or not at all in certain cases.

### Reproduction

```markdown
This is ~~strikethrough text~~ that should be crossed out.

Multiple ~~words~~ with ~~strikethrough~~ formatting.
```

The strikethrough markers don't seem to be properly recognized and the text renders without the strikethrough effect. This affects both single and multiple instances of strikethrough in the same content.

### Expected behavior

Text enclosed in double tildes (`~~text~~`) should render with a strikethrough line through it, following the GFM specification for strikethrough formatting.

### Additional context

This seems to have started occurring recently. The strikethrough syntax worked fine before but now the formatting is inconsistent or missing entirely when rendering markdown content.

---
Repository: /testbed
