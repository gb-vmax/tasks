# Bug Report

### Describe the bug

I'm encountering an issue with MDX tag parsing where component tags with member expressions are not being processed correctly. It seems like the parser is failing to properly handle tags that use dot notation for accessing component properties.

### Reproduction

```mdx
<Component.Member />
```

When trying to use a component with a member accessor (dot notation), the parsing doesn't work as expected. The tag name tokens appear to be exiting in the wrong order, which causes the parser to fail or produce incorrect results.

### Expected behavior

MDX should correctly parse component tags that use member expressions, like `<Component.Member>` or `<Namespace.Component>`. The parser should properly tokenize the component name, the dot separator, and the member name in the correct sequence.

### Additional context

This appears to be related to how the parser handles the token lifecycle when encountering a `.` character in a tag name. The issue manifests when using namespaced or member-accessed components, which is a common pattern in React/JSX.

---
Repository: /testbed
