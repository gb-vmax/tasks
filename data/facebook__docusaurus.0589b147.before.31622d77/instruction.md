# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX flow tag parsing where the tag names and attributes appear to be incorrectly ordered or swapped in the output. When parsing JSX flow tags in MDX content, the primary tag name and local tag name seem to be reversed, causing unexpected behavior in the parsed AST.

### Reproduction

```mdx
<Component.Member prop="value">
  Content here
</Component.Member>
```

When parsing the above MDX content, the tag structure is not being recognized correctly. The component member access notation and namespaced attributes are being parsed in the wrong order.

### Expected behavior

The parser should correctly identify:
- Primary tag name components
- Member/namespaced tag components  
- Attribute names and their prefixes
- Tag name locals vs primaries

in the proper order when constructing the AST for JSX flow tags.

### Additional context

This seems to affect how the MDX parser tokenizes and structures JSX flow elements. The issue manifests when using:
- Namespaced components (e.g., `<namespace:Component>`)
- Member access in component names (e.g., `<Component.Member>`)
- Complex attribute structures

The parsed output doesn't match what would be expected from standard JSX parsing behavior.

---
Repository: /testbed
