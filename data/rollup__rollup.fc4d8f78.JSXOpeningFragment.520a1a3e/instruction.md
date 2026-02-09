# Bug Report

### Describe the bug

I'm encountering an issue with JSX fragment rendering when using nested fragment imports. The fragment variable name is being duplicated in the output, causing incorrect references.

### Reproduction

```jsx
import { Fragment } from 'react';

function MyComponent() {
  return (
    <>
      <div>Content</div>
    </>
  );
}
```

When the JSX fragment is transpiled, the generated code contains duplicate fragment path segments. For example, if the fragment path should be `Fragment.Something`, it appears as `Fragment.Fragment.Something` instead.

### Expected behavior

The fragment variable should be referenced correctly without duplication. The transpiled output should use the proper fragment reference based on the import source.

### Additional context

This seems to affect cases where custom JSX import sources are configured. The fragment path is being constructed incorrectly, leading to runtime errors when the duplicated path doesn't exist on the fragment object.

---
Repository: /testbed
