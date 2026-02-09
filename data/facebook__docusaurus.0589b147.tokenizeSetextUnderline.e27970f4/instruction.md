# Bug Report

### Describe the bug

I'm experiencing an issue with setext heading underlines in markdown parsing. When I have certain content structures before a setext heading (heading with underline using `===` or `---`), the parser seems to be incorrectly identifying what counts as a valid paragraph before the underline.

### Reproduction

```markdown
Some text
with content
===
```

The parser appears to be checking through previous events in the tokenizer but doesn't stop at the right point when determining if there's a valid paragraph before the setext underline. This causes inconsistent behavior where some valid setext headings are not recognized properly, or invalid ones are accepted.

### Expected behavior

The parser should correctly identify whether the content before a setext underline constitutes a valid paragraph by stopping at the first non-lineEnding/linePrefix/content event type. Currently it seems to be continuing through the loop even after finding the relevant event type.

### System Info
- remark version: 15.0.1
- Parser: micromark

---
Repository: /testbed
