# Bug Report

### Describe the bug

I'm encountering an issue with MDX rendering where the layout wrapper is not being applied correctly. When using MDX components with a custom layout, the content appears to be missing or not rendering as expected.

### Reproduction

```jsx
import { MDXProvider } from '@mdx-js/react'

const CustomLayout = ({ children }) => (
  <div className="custom-layout">
    {children}
  </div>
)

// MDX file with layout
export default CustomLayout

# My Content

This is my MDX content.
```

After processing, the MDX content doesn't render properly. The layout wrapper seems to be incomplete or malformed.

### Expected behavior

The MDX content should be wrapped in the custom layout component and render correctly. The JSX structure should include both the layout wrapper and the content inside it.

### Additional context

This appears to have started happening recently. The generated JSX output seems truncated or incomplete. When inspecting the compiled output, the MDXContent function declaration appears to be cut off mid-way through the AST generation.

---
Repository: /testbed
