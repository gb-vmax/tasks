# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with 6 hash marks (`######`) are not being recognized correctly. It seems like the parser is rejecting valid level 6 headings.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6
```

When parsing the above markdown, the level 6 heading (`######`) doesn't get parsed as a heading. It appears to be treated as regular text or rejected by the tokenizer.

### Expected behavior

All headings from level 1 through level 6 should be properly recognized and parsed. According to the CommonMark spec, ATX headings support 1-6 hash marks for heading levels 1-6.

The `###### Heading 6` should be parsed as a valid heading element, just like the other heading levels.

### Additional context

This appears to be affecting the `tokenizeHeadingAtx` function in the MDX parser. Valid level 6 headings are being rejected when they should be accepted.

---
Repository: /testbed
