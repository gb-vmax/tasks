# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX attribute values where literal attribute values are not being set correctly on JSX elements. When parsing MDX content with JSX tags that have quoted attribute values, the attributes seem to be getting lost or overwritten.

### Reproduction

```jsx
// MDX content
<MyComponent title="Hello World" />
```

When this is parsed, the `title` attribute value doesn't appear to be properly assigned to the component. Instead of getting the expected attribute object with a value property, something seems to be going wrong during the parsing phase.

### Expected behavior

The JSX tag should have its attributes properly populated with the literal string values. For example, parsing `<MyComponent title="Hello World" />` should result in an attribute object where the title attribute has the value "Hello World".

### Additional context

This appears to be related to how literal attribute values (quoted strings) are being processed during the MDX parsing. The issue manifests when using standard JSX syntax with string literals as attribute values.

---
Repository: /testbed
