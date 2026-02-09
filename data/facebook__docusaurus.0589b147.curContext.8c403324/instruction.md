# Bug Report

### Describe the bug

I'm experiencing unexpected parsing errors when using MDX with certain JavaScript expressions. The parser seems to be losing track of the correct context, leading to incorrect syntax validation.

### Reproduction

```jsx
const MyComponent = () => {
  return (
    <div>
      {items.map(item => (
        <span key={item.id}>{item.name}</span>
      ))}
    </div>
  )
}
```

When trying to parse this MDX content, the parser throws errors about unexpected tokens or mismatched braces, even though the syntax is valid JSX.

### Expected behavior

The MDX parser should correctly handle nested JSX expressions and maintain proper context tracking. Valid JSX/JavaScript code should parse without errors.

### Additional context

This seems to affect code with nested braces or complex expressions. Simpler examples work fine, but anything with multiple levels of nesting fails to parse correctly.

- MDX version: 3.0.0
- Parser appears to be getting confused about brace context

---
Repository: /testbed
