# Bug Report

### Describe the bug

I'm experiencing an issue with MDX component resolution where components defined in the scope are not being properly recognized. It seems like the logic for determining when to add component references is inverted - components that should be available are being filtered out instead of being included.

### Reproduction

```jsx
import { MDXProvider } from '@mdx-js/react'

const components = {
  h1: CustomH1,
  p: CustomParagraph
}

function App() {
  return (
    <MDXProvider components={components}>
      <MyMDXContent />
    </MDXProvider>
  )
}
```

When rendering MDX content with custom components passed through the provider, the components are not being applied correctly. Instead of using the custom components from the provider, the default HTML elements are rendered.

### Expected behavior

Custom components passed through `MDXProvider` should be used when rendering MDX content. The component resolution logic should properly identify and include components from the provider scope.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: 18.x

---
Repository: /testbed
