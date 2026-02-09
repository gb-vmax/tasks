# Bug Report

### Describe the bug

I'm encountering an issue with parsing ATX headings (markdown headings with `#` symbols) where whitespace handling appears to be broken. When there are spaces in certain positions within the heading, the parser seems to get stuck or behave unexpectedly.

### Reproduction

```markdown
# Heading with spaces
## Another heading
```

When parsing markdown with ATX headings that contain whitespace, the tokenizer doesn't properly handle the spacing between the `#` symbols and the heading text. The issue seems to affect how the parser transitions between states when encountering whitespace characters.

### Expected behavior

The parser should correctly tokenize ATX headings regardless of whitespace positioning. Headings with spaces should be parsed cleanly without the parser entering an incorrect state or infinite loop.

### Additional context

This appears to be related to the `atBreak` function in the heading tokenizer. The whitespace handling logic doesn't seem to be working as intended, which causes problems when processing headings with spaces.

---
Repository: /testbed
