# Bug Report

### Describe the bug

I'm encountering an issue with MDX tag parsing where self-closing tags are not being recognized properly. It seems like the parser is treating the `/` character incorrectly when it appears before the closing `>` in JSX-style tags.

### Reproduction

```mdx
<MyComponent />
```

When trying to parse a self-closing tag like the above, the parser fails to recognize it as valid syntax. The tag should be parsed as a self-closing element, but instead it appears to be treated as an invalid character sequence.

### Expected behavior

Self-closing tags with the `/` character should be properly recognized and parsed as valid MDX/JSX syntax. The parser should accept `<Component />` as a valid self-closing tag.

### Additional context

This affects any self-closing JSX components in MDX files. Standard HTML-style self-closing tags like `<br/>` and React component tags like `<CustomComponent />` are not being parsed correctly.

---
Repository: /testbed
