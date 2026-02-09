# Bug Report

### Describe the bug
When parsing MDX with multiple JSX attributes, only the first attribute gets its name set correctly. All subsequent attributes end up with the wrong name value because they're all trying to write to the first attribute in the array instead of the last one that was added.

### Reproduction
```jsx
<Component 
  firstProp="value1"
  secondProp="value2"
  thirdProp="value3"
/>
```

When this JSX is parsed, all three attributes end up with `name: "thirdProp"` instead of having their respective names.

### Expected behavior
Each attribute should have its own name:
- First attribute: `name: "firstProp"`
- Second attribute: `name: "secondProp"`
- Third attribute: `name: "thirdProp"`

Instead, what happens is all attributes get assigned the name of the last attribute that was processed.

### System Info
- remark-mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
