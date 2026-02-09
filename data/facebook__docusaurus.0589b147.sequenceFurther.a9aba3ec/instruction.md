# Bug Report

### Describe the bug

ATX headings (headings with `#` symbols) are not being parsed correctly. When using multiple `#` symbols to create headings of different levels, the parser seems to be consuming characters incorrectly and not properly recognizing the heading sequence.

### Reproduction

```markdown
## Level 2 Heading
### Level 3 Heading
#### Level 4 Heading
```

When parsing markdown with ATX-style headings, the heading sequences aren't being tokenized properly. The issue appears to be in how the parser handles the sequence of `#` characters - it's not correctly identifying where the heading sequence ends and the heading text begins.

### Expected behavior

The parser should correctly identify the heading level based on the number of `#` symbols (1-6) and properly separate the heading sequence from the heading text. For example:
- `## Heading` should be recognized as a level 2 heading with text "Heading"
- `### Heading` should be recognized as a level 3 heading with text "Heading"

### Additional context

This seems to affect all ATX-style headings regardless of level. The tokenization logic for the heading sequence appears to be inverted or incorrect.

---
Repository: /testbed
