# Bug Report

### Describe the bug

I'm encountering an issue with identifier parsing in MDX content. When using certain JavaScript keywords (specifically `class` and `function`) as identifiers in my MDX files, they're not being parsed correctly and causing unexpected behavior.

### Reproduction

```mdx
export const class = 'my-class'
export const function = 'my-function'

# My Document

Some content here
```

When trying to use these identifiers, they seem to be treated incorrectly during the parsing phase. The parser appears to be rejecting valid identifier names in certain contexts where they should be allowed.

### Expected behavior

JavaScript keywords should be parseable as identifiers when used in valid contexts (like after a dot operator or in certain declaration contexts). The parser should correctly distinguish between keyword usage and identifier usage based on the surrounding context.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems to have broken recently and is preventing me from using certain property names in my MDX files. Any help would be appreciated!

---
Repository: /testbed
