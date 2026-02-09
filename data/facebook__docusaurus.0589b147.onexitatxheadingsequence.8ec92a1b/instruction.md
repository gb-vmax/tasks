# Bug Report

### Describe the bug

I'm experiencing an issue with ATX heading parsing in MDX content. When using ATX-style headings (headings with `#` symbols), the heading depth is not being set correctly. It seems like the parser is failing to properly detect and assign the heading level.

### Reproduction

```mdx
# Heading 1
## Heading 2
### Heading 3
```

When parsing the above MDX content, the headings are not being assigned the correct depth values. The heading nodes appear to be missing their depth property or it's not being set at all.

### Expected behavior

Each ATX heading should have its depth property set based on the number of `#` symbols:
- `#` should have depth 1
- `##` should have depth 2
- `###` should have depth 3
- etc.

The parser should correctly count the number of hash symbols in the ATX heading sequence and assign that value to the heading node's depth property.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
