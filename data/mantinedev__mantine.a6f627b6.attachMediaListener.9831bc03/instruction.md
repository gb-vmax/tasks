# Bug Report

### Describe the bug

The `useMediaQuery` hook is not responding to media query changes. When the viewport size changes (e.g., resizing the browser window or rotating a mobile device), the hook doesn't update its return value even though the media query condition has changed.

### Reproduction

```jsx
import { useMediaQuery } from '@mantine/hooks';

function MyComponent() {
  const isMobile = useMediaQuery('(max-width: 768px)');
  
  return <div>{isMobile ? 'Mobile view' : 'Desktop view'}</div>;
}
```

Steps to reproduce:
1. Render a component using `useMediaQuery`
2. Resize the browser window to cross the breakpoint threshold
3. The component doesn't re-render and still shows the old value

### Expected behavior

The hook should detect media query changes and trigger a re-render with the updated value. For example, when resizing from desktop to mobile viewport, `isMobile` should change from `false` to `true`.

### System Info
- @mantine/hooks version: latest
- Browser: Chrome/Firefox/Safari (affects all browsers)
- React version: 18.x

---
Repository: /testbed
