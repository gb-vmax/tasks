# Bug Report

### Describe the bug

I'm experiencing an issue with emphasis/attention markers (like `*` and `_`) in MDX content. The opening and closing logic for these markers seems to be incorrect, causing them to not be properly recognized in certain contexts.

### Reproduction

```mdx
Text with *emphasis* should work.

But in some cases like:
_emphasis after punctuation_ doesn't render correctly.

Also edge cases with:
*mixed* _markers_ behave unexpectedly.
```

When parsing the above MDX content, the emphasis markers are not being applied correctly. It seems like the logic for determining whether a marker should open or close an emphasis span is broken.

### Expected behavior

Emphasis markers should properly open and close based on the surrounding characters. The parser should correctly identify when `*` or `_` should start or end an emphasis span according to CommonMark rules.

For example:
- `*emphasis*` should render with emphasis
- `_emphasis_` should render with emphasis  
- Markers should work correctly after punctuation or whitespace

### System Info

- MDX version: 3.0.0
- Node version: Latest

This seems to have started recently. The emphasis rendering was working fine before but now certain combinations of text and markers don't parse correctly.

---
Repository: /testbed
