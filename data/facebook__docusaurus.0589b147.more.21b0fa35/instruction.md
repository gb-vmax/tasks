# Bug Report

### Describe the bug

Strikethrough markdown syntax is not rendering correctly in certain cases. When using double tildes (`~~`) to mark text for strikethrough, the text is not being properly formatted.

### Reproduction

```markdown
This ~~should be strikethrough~~ text.
```

Expected the text between the tildes to be rendered with strikethrough formatting, but it's appearing as plain text instead.

### Steps to reproduce:
1. Write markdown with strikethrough syntax using `~~text~~`
2. Render the markdown
3. The strikethrough formatting doesn't apply

### Expected behavior
Text enclosed in double tildes should render with strikethrough formatting according to GFM (GitHub Flavored Markdown) specification.

### Additional context
This seems to have started happening recently. The strikethrough syntax worked fine before but now it's inconsistent. Sometimes it works, sometimes it doesn't - not sure what the pattern is.

---
Repository: /testbed
