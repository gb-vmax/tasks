# Bug Report

### Describe the bug

I'm experiencing an issue with MDX component destructuring when using `MDXLayout`. The generated code seems to be treating the `wrapper` property incorrectly, causing it to be destructured as a getter instead of a regular property.

### Reproduction

```jsx
import { MDXLayout } from './components'

export default function MyMDXContent() {
  // When MDX tries to destructure components
  const { wrapper } = props.components
  // The wrapper is being treated as a getter property
}
```

The issue appears when MDX processes the component imports and tries to map `MDXLayout` to `wrapper`. The destructuring pattern is being generated with the wrong property kind.

### Expected behavior

`MDXLayout` should be destructured as a normal property with `shorthand: false` since it's being renamed to `wrapper`. The current behavior is generating inconsistent property definitions in the object pattern.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest

---
Repository: /testbed
