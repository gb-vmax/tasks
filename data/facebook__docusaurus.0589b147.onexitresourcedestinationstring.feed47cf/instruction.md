# Bug Report

### Describe the bug

I'm experiencing an issue with MDX link parsing where the URL is not being correctly extracted from markdown links. When I use standard markdown link syntax, the resulting link element seems to have incorrect or missing URL data.

### Reproduction

```mdx
[Link text](https://example.com)
```

When this gets parsed, the link's `url` property doesn't contain the expected destination. It seems like the URL is either missing or pointing to the wrong data.

### Expected behavior

The link should render with the correct `href` pointing to `https://example.com`. The parser should correctly extract and assign the URL from the markdown link syntax.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
