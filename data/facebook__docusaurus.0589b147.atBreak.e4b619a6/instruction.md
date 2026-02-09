# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in MDX. When I use hash symbols (`#`) in markdown headings, they're not being recognized correctly. The heading sequence detection seems to be inverted - it's triggering when it shouldn't and not triggering when it should.

### Reproduction

```md
# This is a heading

## This is a level 2 heading

### Level 3 heading
```

When parsing the above markdown, the headings are not being processed as expected. The parser appears to be treating non-hash characters as the start of heading sequences instead of actual hash symbols.

### Expected behavior

Standard ATX headings (using `#` symbols) should be parsed correctly:
- `#` should create a level 1 heading
- `##` should create a level 2 heading
- `###` should create a level 3 heading
- etc.

The heading text should be properly extracted and the heading structure should be maintained.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This seems like a logic error in the tokenizer where the condition for detecting hash symbols got flipped somehow.

---
Repository: /testbed
