# Bug Report

### Describe the bug

The Combobox component is not filtering options when a search string is provided. The dropdown shows all options regardless of what's typed in the search field.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const data = [
  { value: 'apple', label: 'Apple' },
  { value: 'banana', label: 'Banana' },
  { value: 'cherry', label: 'Cherry' }
];

function Demo() {
  const [search, setSearch] = useState('');
  
  return (
    <Combobox>
      <Combobox.Target>
        <input 
          value={search} 
          onChange={(e) => setSearch(e.target.value)}
        />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Options>
          <OptionsDropdown data={data} search={search} />
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

When typing "app" in the input, all three options are still displayed instead of just "Apple".

### Expected behavior

When a search string is provided, the options should be filtered to only show matching results. In the example above, typing "app" should only display the "Apple" option.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
