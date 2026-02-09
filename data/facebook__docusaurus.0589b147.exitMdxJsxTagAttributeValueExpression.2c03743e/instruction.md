# Bug Report

### Describe the bug

I'm encountering an issue with MDX JSX tag attribute value expressions. When using expression values in JSX attributes, the parser seems to be assigning the value to the wrong attribute in the AST.

### Reproduction

```jsx
<Component 
  first="static"
  second={dynamicValue}
  third="another"
/>
```

When parsing MDX with multiple attributes where one has an expression value, the expression gets attached to an incorrect attribute. It appears the parser is looking at the wrong position in the attributes array.

### Expected behavior

Each attribute should correctly receive its own value. Expression values should be assigned to the attribute they're defined on, not a different one.

### Additional context

This affects any MDX component that has:
- Multiple attributes
- At least one attribute with an expression value (curly braces)

The issue seems related to how the AST is being constructed during the parsing phase.

---
Repository: /testbed
