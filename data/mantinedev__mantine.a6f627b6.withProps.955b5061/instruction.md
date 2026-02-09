# Bug Report

### Describe the bug

The `withProps` method is returning the wrong type. It's supposed to return a `React.ForwardRefExoticComponent` but instead it's returning the result of `React.forwardRef` directly, which breaks the type signature and causes runtime issues.

### Reproduction

```tsx
const Button = factory<ButtonFactory>((_props, ref) => {
  return <button ref={ref}>Click me</button>;
});

// Using withProps
const StyledButton = Button.withProps({ 
  className: 'custom-style' 
});

// This causes type errors and runtime issues
<StyledButton onClick={() => console.log('clicked')} />
```

### Expected behavior

The `withProps` method should return a properly typed `ForwardRefExoticComponent` that can be used like any other Mantine component. The component should accept all the original props merged with the default props provided to `withProps`.

### System Info
- @mantine/core version: latest
- React version: 18.x
- TypeScript version: 5.x

---
Repository: /testbed
