# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing where the heading sequence is not being properly recognized. When parsing markdown with ATX-style headings (using `#` symbols), the parser seems to be entering the wrong token state and returning prematurely.

### Reproduction

```markdown
# Heading 1
## Heading 2
### Heading 3
```

When processing ATX headings, the tokenizer appears to skip the sequence parsing step entirely. The `before` function is now entering `atxHeading` twice (once in the initial function and once in `before`) and returning the code directly instead of continuing to `sequenceOpen`.

### Expected behavior

The tokenizer should:
1. Enter the `atxHeading` state once
2. Enter the `atxHeadingSequence` state
3. Process the sequence of `#` characters through `sequenceOpen`
4. Properly tokenize the heading level based on the number of `#` symbols

Instead, it's bypassing the sequence tokenization entirely.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
