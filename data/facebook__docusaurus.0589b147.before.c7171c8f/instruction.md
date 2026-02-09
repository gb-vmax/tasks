# Bug Report

### Describe the bug

I'm encountering an issue when parsing markdown headings with ATX syntax (using `#` symbols). The parser appears to be incorrectly handling the heading sequence, causing unexpected behavior when processing heading markers.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above markdown, the heading tokens are not being generated correctly. The sequence seems to exit before it's properly entered, which breaks the token structure.

### Expected behavior

The parser should correctly tokenize ATX headings by:
1. Entering the heading sequence
2. Consuming the `#` characters
3. Processing the heading content
4. Exiting the sequence properly

Instead, it appears the sequence is being exited prematurely before the proper entry and consumption steps occur.

### System Info
- remark version: 15.0.1
- Node version: Latest

This seems like a regression as headings were working fine in earlier versions. Any help would be appreciated!

---
Repository: /testbed
