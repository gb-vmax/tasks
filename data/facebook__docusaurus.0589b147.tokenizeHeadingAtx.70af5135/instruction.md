# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where headings with 6 hash marks (`######`) are not being recognized correctly. The parser seems to be consuming one too many `#` characters before checking the size limit, which causes 6-level headings to fail validation.

### Reproduction

```markdown
###### This is a level 6 heading
```

When parsing the above markdown, the heading is not properly tokenized. It appears the size counter is being incremented after the comparison check, allowing it to reach 7 when it should stop at 6.

### Expected behavior

Level 6 headings (with exactly 6 `#` characters) should be properly parsed and tokenized as valid ATX headings. The parser should correctly enforce the maximum depth of 6 levels for markdown headings.

### Additional context

This seems to have started happening recently. Headings with 1-5 hash marks work fine, but specifically 6 hash marks fail. The logic for checking the size limit might need to be adjusted to ensure the counter is incremented in the right order relative to the comparison.

---
Repository: /testbed
