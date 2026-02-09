# Bug Report

### Describe the bug

I'm experiencing an issue with MDX ESM imports/exports parsing. When trying to parse MDX files that contain ESM syntax (like `import` or `export` statements), the parser appears to get confused and produces incorrect AST nodes or fails to properly recognize the ESM blocks.

### Reproduction

```mdx
export const metadata = {
  title: 'My Document'
}

# Hello World

Some content here.
```

When parsing this MDX content, the ESM export block is not being handled correctly. The AST structure seems malformed and the metadata export is either missing from the output or placed in the wrong position in the tree.

### Expected behavior

The parser should correctly identify and process ESM import/export statements at the top level of MDX documents, creating proper AST nodes that represent these code blocks separately from the markdown content.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
