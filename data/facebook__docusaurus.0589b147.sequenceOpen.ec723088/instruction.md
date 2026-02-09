# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing in MDX. When I use headings with spaces in the opening sequence (like `# # # Heading`), the parser is accepting them as valid headings when it shouldn't. This is causing unexpected behavior in my markdown documents.

### Reproduction

```markdown
# # # This should not be a valid heading
```

The above markdown is being parsed as a valid heading, but according to the CommonMark spec, ATX headings should have a continuous sequence of `#` characters without spaces in between.

### Expected behavior

The parser should reject headings that have spaces within the opening `#` sequence. Only continuous sequences like `###` should be recognized as valid ATX heading markers.

For example:
- `### Valid Heading` ✓ should work
- `# # # Invalid Heading` ✗ should not be parsed as a heading

### Additional context

This seems to affect the tokenization logic for ATX headings. The parser is incorrectly treating spaces (character code 32) the same way it treats hash marks (character code 35) in the opening sequence.

---
Repository: /testbed
