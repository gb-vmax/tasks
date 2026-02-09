# Bug Report

### Describe the bug

I've encountered an issue with setext heading parsing where line endings are not being handled correctly. After some changes, it seems like there's a problem with how the parser tracks whether to consume line endings after setext heading text.

### Reproduction

```markdown
Heading
=======

Next paragraph
```

When parsing the above markdown, the behavior seems inconsistent. The setext heading (underlined with `=`) doesn't properly handle the line ending, which can cause issues with subsequent content parsing.

### Expected behavior

The parser should correctly track and handle line endings after setext heading text, ensuring that the next content (like paragraphs) is properly separated and parsed.

### Additional context

This appears to be related to how the internal state flag for setext headings is being set. The issue manifests when parsing setext-style headings (those using `===` or `---` underlines) followed by other content.

---
Repository: /testbed
