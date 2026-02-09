# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag attribute value expressions. When using multiple attributes with expression values on a JSX component, only the first attribute gets the expression value assigned correctly. All subsequent attributes with expression values seem to overwrite the first attribute's value instead of being assigned to their respective attributes.

### Reproduction

```mdx
<Component 
  first={someValue}
  second={anotherValue}
  third={yetAnotherValue}
/>
```

When parsing this, all three attributes end up with the same expression value (the last one), or the values get assigned to the wrong attributes. The expected behavior would be that each attribute receives its corresponding expression value.

### Expected behavior

Each attribute should maintain its own expression value independently. The `first` attribute should have `someValue`, `second` should have `anotherValue`, and `third` should have `yetAnotherValue`.

### Additional context

This seems to affect JSX components with multiple attributes that use expression syntax. Single-attribute components work fine, but as soon as you add a second attribute with an expression value, the behavior becomes incorrect.

---
Repository: /testbed
