# Bug Report

### Describe the bug

Strikethrough syntax in markdown is not being parsed correctly. Text wrapped with double tildes (`~~text~~`) is not being recognized as strikethrough, and the tildes are being rendered as literal characters instead.

### Reproduction

```markdown
This is ~~strikethrough~~ text.
```

Expected output: The word "strikethrough" should be rendered with a strikethrough style.

Actual output: The text renders as "This is ~~strikethrough~~ text." with the tildes visible.

### Additional context

This seems to affect the GFM (GitHub Flavored Markdown) strikethrough extension. The issue appears when trying to use standard strikethrough syntax. Single tilde strikethrough also doesn't work as expected.

Example that should work:
```markdown
~~This should be struck through~~
```

But instead the tildes are just displayed as regular text characters.

---
Repository: /testbed
