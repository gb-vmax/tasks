# Bug Report

### Describe the bug

When using `OptionsDropdown` with `filterOptions` prop, the search filtering behavior is inverted. Setting `filterOptions={true}` results in no filtering being applied, while `filterOptions={false}` causes the options to be filtered by the search term.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function Demo() {
  const [search, setSearch] = useState('');
  
  return (
    <Combobox>
      <Combobox.Target>
        <TextInput 
          value={search} 
          onChange={(e) => setSearch(e.currentTarget.value)} 
        />
      </Combobox.Target>
      <Combobox.Dropdown>
        <OptionsDropdown
          data={['Apple', 'Banana', 'Orange']}
          search={search}
          filterOptions={true}  // Expected to filter, but doesn't
        />
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

### Expected behavior

When `filterOptions={true}`, the dropdown options should be filtered based on the search input. When `filterOptions={false}`, no filtering should occur.

Currently, the behavior is reversed - `filterOptions={true}` shows all options regardless of search input, while `filterOptions={false}` applies filtering.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
