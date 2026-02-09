# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/strong text parsing in MDX content. When using asterisks or underscores for emphasis, the text is not being properly rendered with the correct formatting. It seems like the markers are either being left as plain text or the emphasis boundaries are incorrectly calculated.

### Reproduction

```mdx
This is **bold text** and this is *italic text*.

Multiple **strong** markers in the same line.
```

Expected: The text should render with proper bold and italic formatting.

Actual: The emphasis markers appear to be processed incorrectly, resulting in either malformed output or the markers being treated as literal characters.

### Steps to reproduce

1. Create an MDX file with emphasis syntax (asterisks or underscores)
2. Process the file through the MDX parser
3. Observe that the emphasis/strong sequences are not correctly identified or the boundaries are off

This seems to affect both single and double marker sequences. The issue appears to be related to how the parser calculates the positions of opening and closing emphasis sequences.

### System Info

- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
