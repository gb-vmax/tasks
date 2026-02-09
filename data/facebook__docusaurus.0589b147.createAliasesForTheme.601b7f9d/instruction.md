# Bug Report

### Describe the bug

When swizzling theme components, the `@theme-original` alias is not being created correctly. This prevents swizzled components from importing and wrapping the original theme component.

### Reproduction

1. Swizzle a theme component (e.g., `Footer`)
2. Try to import the original component using `@theme-original/Footer`
3. The import fails because the alias is not registered

Example swizzled component:

```js
import React from 'react';
import OriginalFooter from '@theme-original/Footer';

export default function Footer(props) {
  return (
    <div>
      <OriginalFooter {...props} />
      <div>Custom footer content</div>
    </div>
  );
}
```

### Expected behavior

The `@theme-original` alias should be available for swizzled components so they can import and extend the original theme component. This is essential for the wrapper pattern where you want to add functionality around the original component without completely replacing it.

### System Info
- Docusaurus version: latest
- Node version: 18.x

---
Repository: /testbed
