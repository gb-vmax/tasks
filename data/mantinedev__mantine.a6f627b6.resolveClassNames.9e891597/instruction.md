# Bug Report

### Describe the bug

I'm experiencing an issue with the `classNames` prop where passing an array of classNames doesn't work as expected. When I provide an array of className objects or functions, they're not being applied correctly to the component. It seems like the logic for handling arrays vs single objects is reversed.

### Reproduction

```jsx
import { Button } from '@mantine/core';

// This doesn't work when classNames is an array
<Button
  classNames={[
    { root: 'custom-root' },
    { label: 'custom-label' }
  ]}
>
  Click me
</Button>

// Also, when passing a single classNames object, 
// it seems to be treated as an array instead
<Button
  classNames={{ root: 'my-custom-class' }}
>
  Click me
</Button>
```

### Expected behavior

- When `classNames` is an array, it should iterate through the array and merge all className objects
- When `classNames` is a single object or function, it should be wrapped in an array for processing
- All provided classNames should be properly applied to their respective component parts

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
