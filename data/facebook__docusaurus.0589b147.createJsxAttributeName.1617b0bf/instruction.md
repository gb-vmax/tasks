# Bug Report

### Describe the bug

I'm encountering an issue with JSX attribute names in MDX. When trying to use simple attribute names (like `className` or `data-test`), I'm getting errors about member expressions not being supported, even though I'm not using any member expressions.

### Reproduction

```jsx
<div className="test" data-id="123">
  Content here
</div>
```

This throws an error: "Member expressions in attribute names are not supported"

The same happens with any standard HTML/JSX attribute:
```jsx
<button onClick={handler}>Click me</button>
<input type="text" />
<img src="image.png" alt="description" />
```

All of these are failing with the member expression error, which doesn't make sense since none of them are actually using member expressions.

### Expected behavior

Standard JSX attributes should work without throwing errors. Only actual member expressions (like `obj.prop.name`) should trigger the error message.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
