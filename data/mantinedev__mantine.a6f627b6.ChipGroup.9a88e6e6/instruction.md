# Bug Report

### Describe the bug
When using `ChipGroup` with `multiple` mode, the selection behavior is inverted. Clicking on an unselected chip deselects it, and clicking on a selected chip selects it. This makes it impossible to properly select/deselect chips in the group.

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
1. Create a ChipGroup with multiple selection enabled
2. Set an initial value (e.g., `['react']`)
3. Try clicking on an unselected chip (e.g., "Vue")
4. The chip appears unselected instead of selected
5. Try clicking on the initially selected chip ("React")
6. The chip appears selected instead of being deselected

### Expected behavior
- Clicking an unselected chip should select it (add it to the value array)
- Clicking a selected chip should deselect it (remove it from the value array)
- The visual state should match the actual selection state

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
