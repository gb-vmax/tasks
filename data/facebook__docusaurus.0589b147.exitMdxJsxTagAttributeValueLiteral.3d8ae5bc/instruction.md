# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX attribute values where the attributes are not being parsed correctly. When using literal attribute values in JSX tags within MDX files, the values appear to be undefined or incorrectly assigned.

### Reproduction

```mdx
<Component name="test" />
```

When parsing this MDX, the `name` attribute value doesn't get properly assigned to the component. Instead of getting `"test"`, the attribute value ends up being undefined or pointing to the wrong location in the attributes array.

This seems to affect any JSX component with string literal attributes in MDX content.

### Expected behavior

The attribute value should be correctly parsed and assigned. For the example above, the component should receive `name="test"` with the value properly set to the string `"test"`.

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
