# Bug Report

### Describe the bug

I'm experiencing an issue with `ChipGroup` when using it in single-select mode (not multiple). When I click on a chip that's already selected, it doesn't deselect. The chip stays selected even though I expected it to toggle off.

### Reproduction

```jsx
import { ChipGroup, Chip } from '@mantine/core';

function Demo() {
  const [value, setValue] = useState('react');
  
  return (
    <ChipGroup multiple={false} value={value} onChange={setValue}>
      <Chip value="react">React</Chip>
      <Chip value="vue">Vue</Chip>
      <Chip value="angular">Angular</Chip>
    </ChipGroup>
  );
}
```

Steps to reproduce:
1. Click on "React" chip (it becomes selected)
2. Click on "React" chip again
3. Expected: chip should deselect, value should become null/undefined
4. Actual: chip stays selected

### Expected behavior

In single-select mode, clicking an already selected chip should deselect it, similar to how radio buttons or other single-select components work in many UI libraries. The value should become `null` or `undefined` when no chip is selected.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
