# Bug Report

### Describe the bug

I'm encountering an issue with ATX heading parsing where the heading sequence is not being properly tokenized. The parser seems to be skipping the actual consumption of hash characters (`#`) before entering the heading sequence state.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When parsing ATX headings (headings with `#` symbols), the tokenizer appears to be entering the sequence state without actually processing the initial hash character. This causes the heading sequence to be incomplete or malformed.

### Expected behavior

The parser should:
1. Enter the ATX heading state
2. Enter the heading sequence state
3. Consume each `#` character in order
4. Properly track the heading level based on the number of `#` symbols

The heading sequence should be fully captured before moving to the next parsing state.

### Additional context

This affects all ATX-style headings regardless of level (1-6). The tokenization flow seems to have been disrupted, causing the `sequenceOpen` function to be called without the proper code parameter being passed through the state machine.

---
Repository: /testbed
