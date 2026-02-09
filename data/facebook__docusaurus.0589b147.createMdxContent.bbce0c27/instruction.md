# Bug Report

### Describe the bug

After a recent update, MDX documents are not rendering properly when using layouts. The content appears to be completely missing or broken when MDXLayout is involved.

### Reproduction

```jsx
import { MDXProvider } from '@mdx-js/react'

const Layout = ({ children }) => (
  <div className="layout">
    {children}
  </div>
)

// MDX file with layout
export default Layout

# Hello World

This content doesn't render correctly
```

When the MDX file is loaded, the content either doesn't appear or throws an error. This seems to happen specifically when a layout component is defined.

### Expected behavior

The MDX content should render inside the layout component as it did before. The layout should wrap the content and everything should display correctly.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
