# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing where headings are not being recognized correctly. It seems like the heading sequence is not being properly initialized, causing the parser to fail when processing markdown headings.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above markdown, the headings are not being tokenized correctly. The parser appears to be entering the wrong token state during the heading sequence processing.

### Expected behavior

The parser should correctly tokenize ATX headings (headings that start with `#` symbols) and properly enter the `atxHeadingSequence` token before processing the hash symbols. Each heading level should be recognized and parsed according to the markdown spec.

### Additional context

This appears to affect all ATX-style headings regardless of the heading level (1-6). The issue seems related to how the tokenizer enters and processes the heading sequence tokens.

---
Repository: /testbed
