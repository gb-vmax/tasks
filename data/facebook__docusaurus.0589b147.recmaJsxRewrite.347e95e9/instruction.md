# Bug Report

### Describe the bug

I'm experiencing an issue with MDX component resolution where `MDXLayout` is being incorrectly added to the components list. It seems like the logic for checking whether `MDXLayout` is in scope has been inverted, causing unexpected behavior in how layouts are handled.

### Reproduction

```jsx
import { MDXProvider } from '@mdx-js/react'

function MyMDXContent(props) {
  // MDXLayout should not be added to components when it's already in scope
  return <div>Content</div>
}

// When MDXLayout is defined in the current scope,
// it's being added again to the components array
const MDXLayout = ({ children }) => <div className="layout">{children}</div>
```

### Expected behavior

When `MDXLayout` is already defined in the current scope, it should not be added to the components list again. The current behavior appears to do the opposite - it adds `MDXLayout` when it IS in scope rather than when it ISN'T.

Additionally, there seems to be a related issue with reference tracking where the loop iterating over object key parts goes one iteration too far, potentially accessing undefined properties.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
