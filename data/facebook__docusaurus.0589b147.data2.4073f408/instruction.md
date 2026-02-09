# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in MDX where the heading text is not being properly captured. It seems like the parser is exiting the heading text state prematurely or not handling certain character codes correctly.

### Reproduction

```mdx
# My Heading
```

When parsing ATX headings (headings with `#` symbols), the text content appears to be lost or not properly tokenized. The heading sequence is recognized, but the actual heading text doesn't make it through the parsing pipeline.

### Expected behavior

The parser should correctly extract and preserve the heading text content. For example, `# My Heading` should parse with "My Heading" as the heading text, not an empty string or undefined.

### Additional context

This appears to be related to how the `data2` function in `tokenizeHeadingAtx` handles character codes and when it exits the "atxHeadingText" state. The heading structure is recognized but the content seems to be getting dropped during tokenization.

---
Repository: /testbed
