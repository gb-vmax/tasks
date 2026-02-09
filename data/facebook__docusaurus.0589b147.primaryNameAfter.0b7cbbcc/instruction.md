# Bug Report

Title: JSX member access syntax not working after tag names

I'm encountering an issue where using member access (dot notation) on JSX tag names doesn't work as expected. When I try to use a component like `Foo.Bar`, it's not being parsed correctly.

Steps to reproduce:
1. Create an MDX file with a namespaced component using dot notation
2. Try to use it like `<Foo.Bar>content</Foo.Bar>`
3. The component doesn't render properly

Example:
```jsx
const Components = {
  Button: {
    Primary: () => <button>Primary</button>
  }
}

// This doesn't work
<Components.Button.Primary />
```

### Expected behavior
JSX member access syntax (e.g., `<Foo.Bar>`) should be properly parsed and the component should render correctly, just like it does in regular React/JSX.

### Additional context
This seems related to how tag names are being processed. Colon syntax (`:`) for namespaces appears to have the same issue.

---
Repository: /testbed
