# Bug Report

### Describe the bug

I'm experiencing an issue with MDX JSX tag attributes where only the first attribute gets its value set correctly when multiple attributes are present. When I have a component with multiple attributes that have literal values, all attributes after the first one lose their values.

### Reproduction

```mdx
<MyComponent 
  first="value1" 
  second="value2" 
  third="value3" 
/>
```

When parsing this, only `first` gets the value "value1", while `second` and `third` end up with incorrect or missing values. It seems like all attribute values are being assigned to the first attribute instead of the last one being processed.

### Expected behavior

Each attribute should receive its corresponding value:
- `first` should have value "value1"
- `second` should have value "value2"  
- `third` should have value "value3"

Instead, what's happening is that the values are all being set to the first attribute in the array, overwriting each other.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

This seems like a regression as this was working fine in previous versions. Any help would be appreciated!

---
Repository: /testbed
