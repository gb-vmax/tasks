# Bug Report

### Describe the bug

I'm experiencing issues with the Combobox component where the filtering and empty state display are not working as expected. 

When I type in the search field, the options list behavior seems inverted - it's not filtering properly based on my input. Additionally, the "nothing found" message appears at the wrong times.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

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
          <Combobox.Option value="apple">Apple</Combobox.Option>
          <Combobox.Option value="banana">Banana</Combobox.Option>
          <Combobox.Option value="cherry">Cherry</Combobox.Option>
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

### Expected behavior

1. When `filterOptions` is enabled, typing in the search field should filter the options list based on the search query
2. The `nothingFoundMessage` should only display when the filtered results are empty (no matching options found)
3. When there are matching options, the options should be displayed normally

### Actual behavior

1. The filtering doesn't seem to work correctly - options aren't being filtered based on search input
2. The "nothing found" message shows up when there ARE results available, instead of when the list is empty

This makes the component unusable for searchable dropdowns. Any help would be appreciated!

---
Repository: /testbed
