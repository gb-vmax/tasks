# Bug Report

### Describe the bug

I'm encountering an issue with MDX link parsing where links with labels are not being recognized correctly. It seems like the label validation logic is inverted - links that should work are being rejected, while invalid links might be getting through.

### Reproduction

```mdx
[valid link text](https://example.com)

[another link][ref]

[ref]: https://example.com
```

When parsing the above MDX content, valid links with proper label syntax are not being processed correctly. The parser appears to be rejecting links that have a valid `labelStart` token, which is the opposite of what should happen.

### Expected behavior

Links with proper label syntax should be parsed and rendered correctly. The parser should:
1. Accept links when a `labelStart` token exists
2. Reject links when no `labelStart` token is found
3. Properly handle reference-style links with defined references

### Additional context

This appears to affect the `tokenizeLabelEnd` function in the MDX parser. The link validation seems to be checking for the wrong condition when determining whether to proceed with label processing or reject the token.

---
Repository: /testbed
