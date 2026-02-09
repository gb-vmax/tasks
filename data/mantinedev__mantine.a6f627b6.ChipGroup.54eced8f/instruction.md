# Bug Report

### Describe the bug

I'm experiencing an issue with the `ChipGroup` component where chips are showing incorrect selection states. When I click on a chip in single-select mode, the visual state doesn't match what I expect.

### Reproduction

```jsx
import { ChipGroup, Chip } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('react');

  return (
    <ChipGroup value={value} onChange={setValue}>
      <Chip value="react">React</Chip>
      <Chip value="vue">Vue</Chip>
      <Chip value="angular">Angular</Chip>
    </ChipGroup>
  );
}
```

Steps to reproduce:
1. Set an initial value for the ChipGroup (e.g., 'react')
2. Observe that the chip with value 'react' appears unselected
3. Click on the 'react' chip
4. The chip still doesn't appear selected, but other chips do

### Expected behavior

- The chip matching the current value should appear selected
- Clicking on an already selected chip should deselect it
- Clicking on an unselected chip should select it

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
