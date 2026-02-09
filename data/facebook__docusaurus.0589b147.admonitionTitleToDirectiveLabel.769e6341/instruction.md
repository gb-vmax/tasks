# Bug Report

### Describe the bug

When using admonitions with indentation in Markdown files, the title conversion to directive label is not working correctly. The indentation is being captured incorrectly, causing the regex groups to be misaligned.

### Reproduction

```markdown
    :::note My Title
    Content here
    :::
```

When processing this Markdown with `admonitionTitleToDirectiveLabel()`, the indentation and other captured groups are not being extracted properly from the regex match. The function appears to be accessing the wrong argument index for the named groups object.

### Expected behavior

The function should correctly preserve indentation when converting admonition titles to directive labels, maintaining the proper spacing in the output.

### Additional context

This affects any Markdown content that uses indented admonition blocks. The issue seems related to how the regex named capture groups are being accessed from the `replaceAll` callback arguments.

---
Repository: /testbed
