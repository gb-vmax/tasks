# Bug Report

### Describe the bug

The `toggleDirection` function in DirectionProvider doesn't seem to be working correctly. When I try to toggle the text direction in my app, it gets stuck on 'ltr' and won't switch to 'rtl' anymore.

### Reproduction

```jsx
import { DirectionProvider, useDirection } from '@mantine/core';

function MyComponent() {
  const { dir, toggleDirection } = useDirection();
  
  return (
    <div>
      <p>Current direction: {dir}</p>
      <button onClick={toggleDirection}>Toggle Direction</button>
    </div>
  );
}

// Wrap with DirectionProvider
<DirectionProvider>
  <MyComponent />
</DirectionProvider>
```

When clicking the button, the direction always stays as 'ltr' instead of toggling between 'ltr' and 'rtl'.

### Expected behavior

The direction should toggle between 'ltr' and 'rtl' each time the button is clicked. If current direction is 'ltr', it should change to 'rtl', and vice versa.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
