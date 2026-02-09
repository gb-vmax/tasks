# Bug Report

### Describe the bug

I'm experiencing an issue with markdown parsing where label/link references are not being processed correctly. When parsing markdown with reference-style links, the parser seems to be returning incorrect values in certain edge cases, which causes the parsing to fail or produce unexpected results.

### Reproduction

```js
const markdown = `
[link text][ref]

[ref]: https://example.com
`;

// Parser fails to correctly handle the reference
const result = parse(markdown);
```

The issue appears to be related to how the `labelEndOk` callback handles return values when processing label end tokens. In some cases, the function returns an unexpected value instead of properly calling the success callback.

### Expected behavior

The parser should correctly process reference-style links and return the appropriate AST structure. The `labelEndOk` function should always properly invoke the success callback with the code point.

### System Info
- remark version: 15.0.1
- Node version: Latest

---
Repository: /testbed
