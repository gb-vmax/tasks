# Bug Report

### Describe the bug

Strikethrough text is not being rendered correctly in markdown. When using double tildes (`~~text~~`) to create strikethrough formatting, the text appears as plain text instead of being struck through.

### Reproduction

```markdown
This is ~~strikethrough~~ text.

Another example: ~~deleted content~~ should appear crossed out.
```

Expected output: Text between `~~` markers should be rendered with strikethrough formatting.

Actual output: The tildes and text are displayed as-is without any formatting applied.

### Additional context

This seems to have broken recently. The strikethrough syntax was working fine before but now it's just showing the raw markdown instead of processing it. Not sure what changed but it's affecting all strikethrough text in our documentation.

---
Repository: /testbed
