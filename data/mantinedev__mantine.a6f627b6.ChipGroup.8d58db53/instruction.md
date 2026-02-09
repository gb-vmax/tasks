# Bug Report

### Describe the bug

I'm experiencing strange behavior with the `ChipGroup` component when using it in multiple selection mode. The chips are showing the opposite selection state - when a chip should be selected, it appears unselected, and vice versa. Clicking on chips seems to invert the selection rather than toggling it normally.

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

### Expected behavior

- Initially, the "React" chip should be selected (since it's in the value array)
- Clicking on "React" should deselect it
- Clicking on "Vue" should add it to the selection
- The visual state should match the actual value

### Actual behavior

- The "React" chip appears unselected even though it's in the value array
- Clicking on an unselected chip deselects it (removes it from value)
- Clicking on a selected chip selects it (adds it to value)
- Everything is backwards

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

This is making the component unusable for multi-select scenarios. Any help would be appreciated!

---
Repository: /testbed
