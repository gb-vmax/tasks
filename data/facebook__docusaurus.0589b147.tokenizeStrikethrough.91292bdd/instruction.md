# Bug Report

### Describe the bug

I'm encountering an issue with strikethrough rendering in GFM (GitHub Flavored Markdown). It seems like strikethrough text with double tildes (`~~text~~`) is not being parsed correctly anymore.

### Reproduction

When trying to use strikethrough syntax in markdown:

```markdown
This is ~~strikethrough text~~ in a sentence.
```

The strikethrough doesn't render properly. The tildes are either showing up as literal characters or the text isn't being struck through as expected.

### Expected behavior

Text enclosed in double tildes (`~~`) should render with a strikethrough effect, like this:
- Input: `~~deleted text~~`
- Expected output: ~~deleted text~~

### Additional context

This used to work fine before, but seems to have broken recently. Single tildes shouldn't trigger strikethrough, only double tildes should work according to GFM spec.

---
Repository: /testbed
