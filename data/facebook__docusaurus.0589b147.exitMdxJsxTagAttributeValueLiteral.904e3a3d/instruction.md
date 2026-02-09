# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag attribute parsing. When using literal values for JSX attributes in MDX files, the wrong attribute is being assigned the value, and the value itself is not being parsed correctly.

### Reproduction

```mdx
<MyComponent foo="bar" baz="qux" />
```

When this MDX is parsed, the attribute values are assigned to the wrong attributes. For example, the value `"bar"` might end up on `baz` instead of `foo`, or vice versa. Additionally, entity parsing seems to be affected - HTML entities in attribute values may not terminate properly.

### Expected behavior

Each attribute should receive its correct literal value, and HTML entities within those values should be properly parsed and terminated. For the example above:
- `foo` should have the value `"bar"`
- `baz` should have the value `"qux"`

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
