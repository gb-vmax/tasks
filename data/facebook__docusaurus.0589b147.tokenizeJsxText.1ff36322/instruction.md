# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX text tag parsing where the token types appear to be in the wrong order. This seems to be affecting how JSX expression attributes are being tokenized in inline/text contexts.

When parsing MDX content with JSX tags that contain expression attributes (like `<Component {...props} />`), the parser doesn't seem to be handling them correctly. The tokenization appears to be happening but the resulting AST has tokens in an unexpected sequence.

### Reproduction

```mdx
Here is some text with <Component {...spreadProps} /> inline JSX.
```

When this gets parsed, the expression attribute tokens seem to be out of order compared to what the parser expects. Specifically, it looks like `mdxJsxTextTagExpressionAttributeMarker` and `mdxJsxTextTagExpressionAttributeValue` are being passed to the factory function in the wrong positions.

### Expected behavior

The JSX text tags should be parsed correctly with expression attributes tokenized in the proper order. The token type parameters should match the expected sequence that the `factoryTag` function uses internally.

### System Info
- Using remark-mdx 3.0.0
- Issue appears to be in the vendored version of the library

This seems like it might be a regression or copy-paste error in the token type ordering. Has anyone else encountered this?

---
Repository: /testbed
