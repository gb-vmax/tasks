# Bug Report

### Describe the bug

I'm experiencing an issue with MDX tag parsing where tags followed by whitespace or line endings are being rejected incorrectly. The parser seems to be failing on valid MDX syntax that should be accepted.

### Reproduction

```mdx
<Component>
  content here
</Component>
```

Or with inline spacing:

```mdx
<Component> some text
```

The parser is not handling the whitespace/line ending after the opening tag marker correctly. It appears to be rejecting valid tags that have whitespace immediately following them.

### Expected behavior

Tags followed by whitespace or line endings should be parsed successfully. This is standard MDX/JSX syntax and should work without issues.

### Additional context

This seems to have started recently. The tag parsing logic appears to have the condition inverted - it's rejecting cases where there IS whitespace when it should be rejecting cases where there ISN'T whitespace.

---
Repository: /testbed
