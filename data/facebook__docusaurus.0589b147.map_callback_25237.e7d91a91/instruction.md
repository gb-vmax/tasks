# Bug Report

### Describe the bug

I'm experiencing an issue with MDX component destructuring where the `wrapper` component is not being properly aliased from `MDXLayout`. The destructuring pattern seems to be inverted - it's treating `MDXLayout` as if it should use shorthand notation instead of being aliased to `wrapper`.

### Reproduction

```jsx
import { MDXLayout } from './components'

// When MDXLayout is used, it should be destructured as:
// const { wrapper: MDXLayout } = components
// But instead it's being destructured incorrectly
```

When using a custom layout component via `MDXLayout`, the component mapping doesn't work as expected. The layout wrapper isn't being applied to the rendered MDX content.

### Expected behavior

When `MDXLayout` is provided in the components object, it should be properly destructured with `wrapper` as the key and `MDXLayout` as the value. Other components should use shorthand notation normally.

### System Info
- @mdx-js/mdx version: 3.0.0
- Node version: Latest LTS

---
Repository: /testbed
