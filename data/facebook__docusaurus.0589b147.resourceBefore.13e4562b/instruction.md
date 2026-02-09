# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where whitespace handling in resource URLs appears to be broken. When there are spaces or line breaks before the URL in a markdown link, the parser doesn't process them correctly.

### Reproduction

```markdown
[link text](   https://example.com)
```

or

```markdown
[link text](
  https://example.com
)
```

### Expected behavior

The parser should handle whitespace before the URL in link resources and correctly parse the link. Both examples above should be recognized as valid markdown links.

### Additional context

This seems to affect the tokenization of link resources specifically. The whitespace before the URL should be consumed before attempting to parse the actual resource URL, but instead it appears the logic is inverted causing the parser to fail on valid markdown syntax.

---
Repository: /testbed
