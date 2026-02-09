# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag attribute values when using literal values (quoted strings). It appears that literal attribute values are not being parsed correctly, and the attributes are either missing or contain unexpected values.

### Reproduction

```mdx
<Component name="test" />
<Component title="Hello World" />
<Component label="Some text with entities like &amp; and &quot;" />
```

When parsing these MDX components, the literal attribute values don't seem to be processed properly. The attributes that should contain string values are not being set correctly.

### Expected behavior

Literal attribute values (values in quotes) should be parsed and set correctly on the component attributes. HTML entities within these values should also be properly decoded (e.g., `&amp;` should become `&`, `&quot;` should become `"`).

### System Info
- remark-mdx version: 3.0.0

---
Repository: /testbed
