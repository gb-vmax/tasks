# Bug Report

### Describe the bug

I'm experiencing an issue with parsing ATX-style headings (headings that use `#` symbols). It seems like headings with multiple `#` characters are not being processed correctly anymore.

### Reproduction

When trying to parse markdown content with ATX headings like:

```markdown
## Heading Level 2
### Heading Level 3
#### Heading Level 4
```

The parser appears to fail or produce unexpected results. Specifically, headings with 2 or more `#` symbols don't seem to be recognized properly.

### Expected behavior

ATX headings should be correctly tokenized regardless of the number of `#` symbols used (up to 6 for valid markdown). The parser should consume the sequence of `#` characters and properly identify the heading level.

### Additional context

This appears to affect all multi-character heading sequences. Single `#` headings might still work, but anything with `##` or more seems broken.

---
Repository: /testbed
