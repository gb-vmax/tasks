# Bug Report

### Describe the bug

I'm having an issue with the `DirectionProvider` component. When I try to toggle the text direction using `toggleDirection()`, nothing happens - the direction stays as 'ltr' and doesn't change to 'rtl' as expected.

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

function App() {
  return (
    <DirectionProvider>
      <MyComponent />
    </DirectionProvider>
  );
}
```

When I click the button, the direction doesn't toggle between 'ltr' and 'rtl'. The console shows no errors, but the UI doesn't update.

### Expected behavior

Clicking the toggle button should switch between 'ltr' and 'rtl' directions, and the component should re-render to reflect the change.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Firefox 121

---
Repository: /testbed
