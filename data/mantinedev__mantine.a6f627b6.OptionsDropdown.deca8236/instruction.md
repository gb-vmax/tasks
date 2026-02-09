# Bug Report

### Describe the bug

I'm experiencing an issue with the Combobox component where the empty state is being shown incorrectly when filtering is enabled. Even when there are options available in the data, the component sometimes displays as empty after filtering.

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
          {/* Options here */}
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

When I type in the search input with `filterOptions` prop, the empty state appears even though matching options exist in the original data. The component seems to be checking if the data is empty before filtering is applied instead of after.

### Expected behavior

The empty state should only be shown when the filtered results are actually empty, not based on the original unfiltered data.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
