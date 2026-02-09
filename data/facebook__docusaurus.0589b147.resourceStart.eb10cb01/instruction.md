# Bug Report

### Describe the bug

I'm experiencing an issue with link parsing in markdown. When I try to use links with resources (like `[text](url)`), the parser seems to be failing or producing incorrect output. The links are not being recognized properly.

### Reproduction

```markdown
[example link](https://example.com)
```

When parsing this markdown, the link is not being processed correctly. It seems like the resource part of the link syntax is being handled incorrectly.

I can also reproduce with inline links:
```markdown
Check out [this page](https://test.com) for more info.
```

### Expected behavior

The markdown parser should correctly parse links with resources and convert them to proper link nodes in the AST. The URL should be extracted and associated with the link text.

### Additional context

This appears to have broken recently. Links without resources (like reference-style links) still work fine, but any link that includes the URL directly in parentheses fails to parse correctly.

---
Repository: /testbed
