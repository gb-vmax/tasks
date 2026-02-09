# Bug Report

### Describe the bug

When using JSX fragments in classic mode, the output is being rendered incorrectly. It appears that the classic mode rendering is falling through and also executing the automatic mode rendering, resulting in unexpected/malformed output.

### Reproduction

```jsx
// Configure rollup with jsx: 'classic'
import { Fragment } from 'react';

function MyComponent() {
  return (
    <>
      <div>First child</div>
      <div>Second child</div>
    </>
  );
}
```

When bundling this code with `jsx: 'classic'` mode configured, the fragment gets rendered with both classic and automatic mode transformations applied, which produces invalid output.

### Expected behavior

JSX fragments should be transformed according to the configured jsx mode only:
- In `classic` mode: Should use `React.createElement(React.Fragment, ...)`
- In `automatic` mode: Should use the automatic JSX runtime

Each mode should be mutually exclusive and not fall through to other modes.

### System Info
- Rollup version: latest
- JSX mode: classic

---
Repository: /testbed
