# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX attribute parsing where attribute values are being assigned to the wrong attributes. When using literal values for JSX attributes in MDX, the value gets assigned to the second-to-last attribute instead of the last attribute that was defined.

### Reproduction

```mdx
<Component first="value1" second="value2" />
```

In this case, `"value2"` is being assigned to the `first` attribute instead of the `second` attribute.

Another example:
```mdx
<MyComponent name="test" id="123" class="active" />
```

The value `"active"` ends up on the `id` attribute instead of the `class` attribute.

### Expected behavior

Attribute values should be assigned to the correct (most recently defined) attribute, not the second-to-last one in the attributes array.

### System Info
- @mdx-js/mdx version: 3.0.0

---
Repository: /testbed
