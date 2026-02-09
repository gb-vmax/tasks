# Bug Report

### Describe the bug

When using components with the `unstyled` prop set to `false` (or not set at all, since it defaults to false), the component styles are not being applied correctly. Instead of getting the proper CSS classes for each selector, it seems like the entire classes object is being returned or styles are missing entirely.

### Reproduction

```jsx
import { Button } from '@mantine/core';

function App() {
  return (
    <Button>
      Click me
    </Button>
  );
}
```

The button renders without any of the expected Mantine styles. When inspecting the element, the CSS classes that should be applied to different parts of the component are either missing or incorrect.

This also happens when explicitly setting `unstyled={false}`:

```jsx
<Button unstyled={false}>
  Click me
</Button>
```

### Expected behavior

Components should render with their default Mantine styles when `unstyled` is `false` or not provided. The proper CSS classes should be applied to each selector/element within the component.

Interestingly, when I set `unstyled={true}`, the component seems to work (just without styles as expected), but the default styled behavior is broken.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
