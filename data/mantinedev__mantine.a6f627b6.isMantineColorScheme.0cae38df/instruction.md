# Bug Report

### Describe the bug

The `isMantineColorScheme` function is not correctly validating color scheme values. When I try to set a valid color scheme like `'dark'` or `'light'`, the validation fails and the color scheme doesn't get applied.

### Reproduction

```js
import { isMantineColorScheme } from '@mantine/core';

// All of these return false even though they should be valid
console.log(isMantineColorScheme('light')); // Expected: true, Actual: false
console.log(isMantineColorScheme('dark'));  // Expected: true, Actual: false
console.log(isMantineColorScheme('auto'));  // Expected: true, Actual: false

// Invalid values also return false (this is correct)
console.log(isMantineColorScheme('invalid')); // Expected: false, Actual: false
```

When trying to use this with `MantineProvider`, the color scheme doesn't get set properly:

```jsx
<MantineProvider theme={{ colorScheme: 'dark' }}>
  <App />
</MantineProvider>
```

The app stays in the default color scheme instead of switching to dark mode.

### Expected behavior

Valid color scheme values (`'light'`, `'dark'`, `'auto'`) should return `true` when passed to `isMantineColorScheme`, and the color scheme should be applied correctly in the provider.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
