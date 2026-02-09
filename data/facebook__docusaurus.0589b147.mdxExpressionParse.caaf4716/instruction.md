# Bug Report

### Describe the bug

I'm encountering an issue with MDX spread element parsing. When using spread syntax in MDX expressions, the parser is incorrectly validating the properties array indices, which causes it to fail on valid spread expressions or accept invalid ones.

### Reproduction

```mdx
{...props}
```

When trying to use a simple spread element like the above, the parser throws errors about extra content or unexpected types even though the spread syntax is valid. The validation logic seems to be checking the wrong array indices when validating spread elements.

### Expected behavior

The parser should correctly validate spread elements by:
1. Checking if there's more than one property (index 1 exists means 2+ properties)
2. Verifying that the first property (index 0) is actually a SpreadElement

Valid single spread expressions like `{...props}` should parse without errors, while expressions with multiple properties or non-spread elements should be properly rejected.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
