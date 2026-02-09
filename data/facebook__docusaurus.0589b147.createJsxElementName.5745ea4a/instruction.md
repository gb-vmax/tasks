# Bug Report

### Describe the bug

I'm encountering an issue where JSX elements are not being rendered properly. When using custom components or elements in MDX files, they appear to be completely missing from the output instead of being rendered as expected.

### Reproduction

```jsx
// Example MDX content
import CustomComponent from './CustomComponent'

<CustomComponent name="test" />

// Expected: Component should render
// Actual: Nothing is rendered, component is missing from output
```

The issue seems to affect any JSX elements, whether they're custom components or standard HTML elements with namespaces. The elements just don't appear in the final output at all.

### Expected behavior

JSX elements should be properly rendered in the output. Custom components and namespaced elements should appear in the compiled result.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

This appears to have started recently, possibly after an update. Any help would be appreciated!

---
Repository: /testbed
