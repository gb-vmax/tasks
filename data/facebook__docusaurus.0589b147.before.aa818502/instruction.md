# Bug Report

### Describe the bug

I'm encountering an issue when parsing ATX-style headings (markdown headings with `#` symbols). The parser seems to be failing when it tries to process the heading sequence, causing an error about exiting a token that was never entered.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When trying to parse any markdown file with ATX headings like the above, the tokenizer throws an error. It appears to be trying to exit the `atxHeadingSequence` token before it's been entered, which breaks the parsing flow.

### Expected behavior

ATX headings should be parsed correctly without errors. The tokenizer should properly enter and exit the `atxHeadingSequence` token in the correct order.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
