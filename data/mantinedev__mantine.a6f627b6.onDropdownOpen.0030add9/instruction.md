# Bug Report

### Describe the bug

The `selectFirstOptionOnDropdownOpen` prop in the Autocomplete component seems to be behaving inversely. When I set it to `true`, the first option is NOT being selected automatically when the dropdown opens. Conversely, when I set it to `false` or leave it undefined, the first option IS being selected.

### Reproduction

```jsx
import { Autocomplete } from '@mantine/core';

function Demo() {
  return (
    <Autocomplete
      data={['React', 'Angular', 'Vue', 'Svelte']}
      selectFirstOptionOnDropdownOpen={true}
      placeholder="Pick a framework"
    />
  );
}
```

Steps to reproduce:
1. Create an Autocomplete with `selectFirstOptionOnDropdownOpen={true}`
2. Click on the input to open the dropdown
3. Notice that no option is highlighted/selected

When I change the prop to `false`, the first option gets selected automatically, which is the opposite of what should happen.

### Expected behavior

When `selectFirstOptionOnDropdownOpen` is set to `true`, the first option should be automatically selected when the dropdown opens. When set to `false`, no option should be selected.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
