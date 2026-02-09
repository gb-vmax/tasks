# Bug Report

### Describe the bug

I'm encountering an issue with MDX tag parsing where tags with no whitespace after the opening angle bracket are not being handled correctly. The parser seems to be rejecting valid tag syntax in certain cases.

### Reproduction

```mdx
<Component/>
```

When trying to parse a self-closing tag like the above, the parser fails to recognize it as valid MDX syntax. This appears to be related to how the parser checks for whitespace immediately after the opening `<` character.

### Expected behavior

Self-closing tags without whitespace after `<` should be parsed correctly, as they are valid JSX/MDX syntax. The component should render normally.

### Additional context

This seems to have broken recently. Tags with attributes or children still work fine, but simple self-closing tags are being rejected. The issue appears to be in the tag marker parsing logic.

---
Repository: /testbed
