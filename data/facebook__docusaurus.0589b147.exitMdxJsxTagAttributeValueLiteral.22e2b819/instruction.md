# Bug Report

### Describe the bug

When parsing MDX files with JSX attributes that have literal values, the attribute value is being assigned to the wrong attribute in the attributes array. It appears that the parsed value is being set on the second-to-last attribute instead of the last one.

### Reproduction

```jsx
<MyComponent 
  firstProp="value1"
  secondProp="value2"
/>
```

When parsing the above MDX, the `secondProp` value ends up assigned to `firstProp` instead. The attributes array indexing seems to be off by one.

### Expected behavior

Each attribute's value should be correctly assigned to its corresponding attribute name. In the example above:
- `firstProp` should have value `"value1"`
- `secondProp` should have value `"value2"`

### Additional context

This issue affects any JSX tags with multiple attributes where at least one has a literal string value. The problem seems to be in how the attribute values are being indexed when they're added to the attributes array.

---
Repository: /testbed
