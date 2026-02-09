# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute value expressions where the wrong attribute is being targeted when setting expression values. It appears that the code is accessing `tag.attributes[tag.attributes.length - 2]` instead of the last attribute, which causes the expression value to be assigned to the incorrect attribute.

### Reproduction

```mdx
<Component 
  firstAttr="value"
  secondAttr={expression}
/>
```

When parsing this MDX, the expression value gets assigned to `firstAttr` instead of `secondAttr`. The issue occurs because the parser is looking at the second-to-last attribute instead of the last one.

### Expected behavior

The attribute value expression should be assigned to the correct (last) attribute in the attributes array. In the example above, `{expression}` should be the value of `secondAttr`, not `firstAttr`.

### Additional context

This seems to affect any MDX component with multiple attributes where at least one uses an expression value. The expression always ends up on the wrong attribute.

---
Repository: /testbed
