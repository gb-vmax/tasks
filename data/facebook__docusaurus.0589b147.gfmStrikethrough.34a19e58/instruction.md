# Bug Report

### Describe the bug

I'm experiencing an issue with strikethrough parsing in the markdown renderer. When using double tildes (`~~`) for strikethrough text, the parsing seems to fail or behave unexpectedly. The text either doesn't get marked as strikethrough or the parser gets stuck.

### Reproduction

```markdown
This is ~~strikethrough text~~ in a sentence.
```

When processing this markdown, the strikethrough doesn't render correctly. It seems like the parser might be having trouble matching the opening and closing tilde sequences.

I also noticed that single tildes might be involved in the issue - not sure if they're supposed to work for strikethrough or if there's some edge case with how the sequences are being matched.

### Expected behavior

The text between `~~` markers should be properly parsed as strikethrough and rendered with the appropriate styling. The opening and closing sequences should match correctly.

### System Info
- Using the GFM (GitHub Flavored Markdown) extension
- remark-gfm version: 4.0.0

---
Repository: /testbed
