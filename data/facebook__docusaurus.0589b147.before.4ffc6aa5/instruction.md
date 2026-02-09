# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing in MDX. The heading tokenizer appears to be incorrectly exiting the `atxHeadingSequence` state multiple times, which causes the parser to fail or produce unexpected results when processing markdown headings.

### Reproduction

```md
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above markdown content, the headings are not being recognized properly. The tokenizer seems to be exiting the heading sequence state prematurely before actually processing the hash characters.

### Expected behavior

The parser should correctly tokenize ATX headings by:
1. Entering the `atxHeadingSequence` state
2. Consuming the hash characters (`#`)
3. Exiting the `atxHeadingSequence` state after processing

Instead, it appears to be exiting the sequence state immediately without consuming the hash characters, leading to malformed heading tokens.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken basic heading parsing functionality. Any markdown file with headings is affected.

---
Repository: /testbed
