# Bug Report

### Describe the bug

The `Translate` component is throwing an error when either `id` or `message` is provided with an empty string. Previously, it was possible to use the component with one of these props set to an empty string as long as the other prop was defined, but now it fails validation.

### Reproduction

```jsx
import Translate from '@docusaurus/Translate';

// This now throws an error but should be valid
<Translate id="" message="Hello World" />

// This also throws an error but should be valid
<Translate id="greeting" message="" />
```

Both cases throw:
```
Error: Docusaurus translation declarations must have at least a translation id or a default translation message
```

### Expected behavior

The component should accept empty strings for either `id` or `message` as long as at least one of them has a non-empty value. Empty strings are valid string values and should not be treated the same as `undefined`.

Only when both `id` and `message` are `undefined` (or both are empty strings) should the error be thrown.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
