# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM import/export statements where the data property is not being properly handled during markdown parsing. When using ESM syntax in MDX files, the parsed AST seems to be missing expected data fields.

### Reproduction

```mdx
export const foo = 'bar'

# My Component

Some content here
```

When this MDX content is parsed, the ESM node in the resulting AST doesn't contain the expected data structure. The `mdxjsEsmData` seems to be lost during the exit phase of parsing.

### Expected behavior

The parser should properly preserve all ESM metadata during the markdown-to-AST transformation process. The data property should be populated correctly for ESM nodes.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
