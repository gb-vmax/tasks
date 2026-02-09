# Bug Report

### Describe the bug

After a recent update, MDX files are failing to render properly. The component structure seems to be broken and I'm getting unexpected output when trying to use MDX content with custom layouts.

### Reproduction

When I try to use an MDX file with a custom layout component:

```jsx
// MyComponent.mdx
export const meta = {
  title: 'Test'
}

# Hello World

Some content here
```

```jsx
// Usage
import MyComponent from './MyComponent.mdx'

function App() {
  return <MyComponent components={{ wrapper: CustomLayout }} />
}
```

The component either doesn't render at all or renders incorrectly. It seems like the MDX content generation is incomplete or malformed.

### Expected behavior

The MDX content should render correctly with the custom layout applied. The component should properly handle both cases - when a layout is provided and when it's not.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x
- Browser: Chrome 120

This was working fine before the latest changes. The MDX compilation seems to be cutting off mid-process.

---
Repository: /testbed
