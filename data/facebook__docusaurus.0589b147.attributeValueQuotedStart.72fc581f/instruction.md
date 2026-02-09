# Bug Report

### Describe the bug
I'm experiencing an issue with parsing MDX attributes that have quoted values. When an attribute has an empty quoted value (like `attribute=""`), the parser seems to crash or behave unexpectedly.

### Reproduction
```mdx
<Component attribute="" />
```

When parsing the above MDX code, the parser doesn't handle the empty quoted attribute value correctly. The attribute value is immediately followed by the closing quote, which should be valid syntax.

### Expected behavior
Empty quoted attribute values should be parsed successfully, just like in regular HTML/JSX:
- `<Component attribute="" />` should be valid
- The attribute should be recognized with an empty string value
- No parsing errors should occur

### System Info
- remark-mdx version: 3.0.0
- Node version: Latest

This seems to have started happening recently. Not sure if this is related to recent changes in the attribute value parsing logic.

---
Repository: /testbed
