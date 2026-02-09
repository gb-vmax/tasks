# Bug Report

### Describe the bug

I'm experiencing an issue with the `ChipGroup` component where the selected state appears to be inverted in multiple mode. When I click on a chip to select it, it appears unselected, and when I click to deselect it, it appears selected instead.

### Reproduction

```jsx
import { ChipGroup, Chip } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState(['react']);

  return (
    <ChipGroup multiple value={value} onChange={setValue}>
      <Chip value="react">React</Chip>
      <Chip value="vue">Vue</Chip>
      <Chip value="angular">Angular</Chip>
    </ChipGroup>
  );
}
```

Steps to reproduce:
1. Set up a ChipGroup with multiple mode enabled
2. Initialize with a default value (e.g., `['react']`)
3. Click on the chip that should be selected
4. Notice that it appears unselected instead of selected

### Expected behavior

- Chips that are in the value array should be visually selected
- Clicking an unselected chip should select it
- Clicking a selected chip should deselect it

### Current behavior

The selection state is reversed - chips in the value array appear unselected, and chips not in the value array appear selected.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
