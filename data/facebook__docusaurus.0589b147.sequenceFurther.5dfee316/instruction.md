# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing in remark where headings with multiple `#` characters are not being tokenized correctly. It appears that the sequence parsing logic stops prematurely after consuming the first `#` character instead of continuing through the entire sequence.

### Reproduction

```markdown
## Heading Level 2
### Heading Level 3
#### Heading Level 4
```

When parsing these headings, the tokenizer seems to only recognize the first `#` in the sequence and then immediately breaks, causing the remaining `#` characters to be treated as part of the heading text rather than as part of the heading sequence itself.

### Expected behavior

The parser should consume all consecutive `#` characters at the beginning of a line as part of the heading sequence (up to 6 for valid ATX headings). All `#` characters should be properly recognized as the heading level indicator, not as text content.

For example:
- `##` should be recognized as a level 2 heading sequence
- `###` should be recognized as a level 3 heading sequence
- And so on...

### System Info

- remark version: 15.0.1
- Node version: Latest

This seems to have broken the fundamental ATX heading parsing behavior. Any help would be appreciated!

---
Repository: /testbed
