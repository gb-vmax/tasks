# Bug Report

### Describe the bug

The `<Translate>` component is throwing an error even when both `id` and `message` props are provided. It seems like the validation logic is too strict now and requires both props to be present instead of just one.

### Reproduction

```jsx
import Translate from '@docusaurus/Translate';

// This now throws an error but should work fine
<Translate id="homepage.title" message="Welcome to my site" />

// This also throws an error
<Translate id="homepage.subtitle">
  Learn more about our project
</Translate>
```

Both of these examples throw:
```
Error: Docusaurus translation declarations must have at least a translation id or a default translation message
```

### Expected behavior

The component should accept either:
- Just an `id` prop
- Just a `message` prop  
- Both `id` and `message` props

It should only throw an error when NEITHER prop is provided.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
