# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where the URL/destination of links is not being set correctly. It seems like the link destination is being applied to the wrong node in the AST, causing links to either not work or point to incorrect locations.

### Reproduction

```mdx
[Click here](https://example.com)

![Alt text](https://example.com/image.png)
```

When parsing the above MDX content, the link destinations aren't being assigned properly. The `url` property on the link/image nodes appears to be missing or set on the wrong element.

### Expected behavior

Links and images should have their destination URLs properly assigned to the correct node in the syntax tree. The parser should correctly extract and assign the URL from the markdown link syntax to the appropriate AST node.

### Additional context

This appears to affect both regular links and image references. The issue might be related to how the resource destination string is being processed during the exit phase of parsing.

---
Repository: /testbed
