# Bug Report

### Describe the bug

I'm experiencing an issue with markdown link and image parsing where certain reference-style links are not being processed correctly. It seems like the parser is removing the wrong tokens or skipping elements during processing, which causes malformed output or missing content.

### Reproduction

```js
const markdown = `
Here is a [reference link][ref] and an ![image][img].

[ref]: https://example.com
[img]: https://example.com/image.png
`;

// Parse the markdown
const result = remark().parse(markdown);

// The output is incorrect - some tokens are missing or in wrong positions
```

When parsing markdown with reference-style links and images, the resulting AST appears to have missing or incorrectly positioned nodes. This affects both `[text][ref]` style links and `![alt][ref]` style images.

### Expected behavior

Reference-style links and images should be parsed correctly with all tokens in their proper positions. The parser should properly identify and process label markers for both links and images without corrupting the token stream.

### System Info
- remark version: 15.0.1
- Node version: 18.x

---
Repository: /testbed
