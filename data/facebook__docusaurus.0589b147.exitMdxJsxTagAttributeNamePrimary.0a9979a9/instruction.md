# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute parsing where attribute names are being assigned to the wrong attribute nodes. When processing JSX attributes with namespaced names (like `xml:lang` or `xlink:href`), the primary name part seems to be getting attached to an incorrect attribute object in the AST.

### Reproduction

```mdx
<Component xml:lang="en" />
```

or

```mdx
<svg>
  <use xlink:href="#icon" />
</svg>
```

When parsing MDX content with namespaced JSX attributes, the attribute name doesn't end up on the correct attribute node. It appears the code is looking at the wrong position in the attributes array when trying to set the name property.

### Expected behavior

The attribute name should be correctly assigned to the most recently added attribute node in the AST. For example, when parsing `xml:lang="en"`, the `xml` part should be attached to the current attribute being processed, not a different one.

### Additional context

This seems to affect any JSX tags that use namespaced attributes. The parsing logic appears to be off by one when accessing the attributes array, which causes the name to be set on the wrong attribute object.

---
Repository: /testbed
