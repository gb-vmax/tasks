# Bug Report

### Describe the bug

The Combobox dropdown filter is not working correctly - it's showing the opposite results of what's expected. When I type in the search box, items that DON'T match my input are being displayed, while items that DO match are being filtered out.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const items = [
  { label: 'Apple', value: 'apple' },
  { label: 'Banana', value: 'banana' },
  { label: 'Cherry', value: 'cherry' },
];

<Combobox>
  <Combobox.Target>
    <input />
  </Combobox.Target>
  <Combobox.Dropdown>
    {items.map(item => (
      <Combobox.Option key={item.value} value={item.value}>
        {item.label}
      </Combobox.Option>
    ))}
  </Combobox.Dropdown>
</Combobox>
```

Steps to reproduce:
1. Create a Combobox with several options
2. Type "app" in the input field
3. Observe that "Banana" and "Cherry" are shown instead of "Apple"
4. Type "ban" and see "Apple" and "Cherry" instead of "Banana"

### Expected behavior

When typing "app", only "Apple" should be visible in the dropdown. When typing "ban", only "Banana" should be visible. The filter should show items that match the input, not items that don't match.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
