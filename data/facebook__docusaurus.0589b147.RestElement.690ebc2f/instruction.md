# Bug Report

### Describe the bug

I think there's a problem with the MDX code generator. When trying to use spread/rest operators in MDX files, I'm getting syntax errors or the code doesn't compile at all.

### Reproduction

```jsx
// In an MDX file
const MyComponent = ({ ...props }) => {
  return <div {...props}>Content</div>
}

// Or with arrays
const arr = [1, 2, 3]
const newArr = [...arr, 4, 5]
```

When I try to compile this, it fails. It seems like the spread operator (`...`) isn't being handled correctly during code generation.

### Expected behavior

The MDX compiler should properly handle rest parameters in function arguments and spread operators in JSX/arrays. The code should compile without errors and the spread syntax should work as expected.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
