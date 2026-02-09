# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading sequence token is being entered twice, which causes incorrect tokenization behavior. This appears to be affecting the parsing of markdown headings that use the `#` syntax.

### Reproduction

```js
// When parsing ATX headings like:
# Heading 1
## Heading 2

// The tokenizer enters the atxHeadingSequence token multiple times
// before actually processing the sequence, leading to malformed tokens
```

### Expected behavior

The `atxHeadingSequence` token should only be entered once per heading, after the initial setup but before consuming the hash characters. The current behavior seems to call `sequenceOpen()` before entering the token, which duplicates the sequence processing.

### Additional context

This is affecting markdown parsing for standard ATX-style headings. The tokenizer flow should be:
1. Enter the heading
2. Enter the sequence token
3. Process/consume the hash characters

But it seems like step 3 is being called before step 2, causing the sequence to be processed incorrectly.

---
Repository: /testbed
