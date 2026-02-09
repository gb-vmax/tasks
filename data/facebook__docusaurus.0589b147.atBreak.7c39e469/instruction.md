# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with trailing `#` characters are not being recognized correctly. It seems like the parser is treating the trailing `#` symbols as part of the heading text instead of as optional closing sequences.

### Reproduction

When parsing markdown with ATX headings that have trailing `#` characters:

```markdown
## Heading with trailing hashes ##
### Another example ###
```

The trailing `##` and `###` are not being properly handled as closing sequences. The parser appears to be checking for the wrong character code when determining if a sequence should continue.

### Expected behavior

ATX headings should support optional closing sequences of `#` characters. The trailing `#` symbols should be recognized and removed from the heading text, leaving just the actual heading content.

For example:
- `## Heading ##` should parse as "Heading"
- `### Test ###` should parse as "Test"

### Additional context

This affects any markdown content that uses the optional closing `#` syntax for ATX headings, which is valid according to the CommonMark spec. The issue seems related to how the tokenizer handles the sequence continuation logic.

---
Repository: /testbed
