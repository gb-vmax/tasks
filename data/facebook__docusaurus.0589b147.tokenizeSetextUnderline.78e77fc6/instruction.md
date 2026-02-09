# Bug Report

### Describe the bug

I'm encountering an issue with setext heading parsing where the parser is incorrectly identifying certain text blocks. It seems like the logic for determining whether a line with underline characters (like `===` or `---`) should be treated as a setext heading is inverted.

### Reproduction

```markdown
This is a paragraph
---

Another paragraph
===
```

When parsing the above markdown, the setext heading detection appears to be behaving incorrectly. Lines that should be recognized as setext headings are not being processed properly, or conversely, lines that shouldn't be treated as headings are being incorrectly identified.

### Expected behavior

The parser should correctly identify setext headings (underlined with `===` for h1 or `---` for h2) and distinguish them from regular paragraphs followed by thematic breaks or other elements.

For example:
- A paragraph followed by `---` or `===` should be converted to a setext heading
- The logic should properly check if the preceding content is a paragraph before treating the underline as a heading marker

### Additional context

This seems to be related to the setext underline tokenization logic. The behavior changed recently and is now producing unexpected results when parsing markdown documents with these heading styles.

---
Repository: /testbed
