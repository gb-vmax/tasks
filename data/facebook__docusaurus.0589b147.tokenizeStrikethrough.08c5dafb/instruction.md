# Bug Report

### Describe the bug

I'm experiencing an issue with strikethrough formatting in markdown. When I try to use double tildes (`~~`) for strikethrough text, it's not being recognized properly. The text that should be struck through is just rendering as plain text with the tildes visible.

### Reproduction

```markdown
This is ~~strikethrough text~~ that should work.

Also trying ~~another example~~ here.
```

When I parse this markdown, the strikethrough syntax isn't being applied. The tildes just show up as literal characters instead of formatting the text.

### Expected behavior

The text between `~~` should be rendered as strikethrough. The double tilde syntax is standard GFM (GitHub Flavored Markdown) and should work for wrapping text that needs to be struck through.

### Additional context

This seems to have started happening recently. I'm using the remark-gfm plugin for parsing GitHub Flavored Markdown. Single tilde usage also doesn't seem to work correctly anymore.

---
Repository: /testbed
