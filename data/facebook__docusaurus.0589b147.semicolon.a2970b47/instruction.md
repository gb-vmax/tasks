# Bug Report

### Describe the bug

I'm experiencing an issue with MDX parsing where semicolons are being handled incorrectly. When parsing JavaScript expressions in MDX files, the parser is throwing unexpected token errors even when the syntax appears to be valid.

### Reproduction

```mdx
export const config = {
  title: 'Test'
};

# Hello World

This is a test MDX file with a valid export statement.
```

When trying to parse this file, I get an unexpected token error. The export statement is valid JavaScript with a proper semicolon, but the parser seems to be rejecting it.

### Expected behavior

The parser should correctly handle JavaScript expressions with semicolons in MDX files. Valid export statements with semicolons should parse without errors.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

This seems to have started happening recently. The same MDX files were parsing fine before. Any help would be appreciated!

---
Repository: /testbed
