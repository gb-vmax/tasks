# Bug Report

### Describe the bug

When using the Combobox component with `filterOptions` enabled, the filtering behavior is inverted - it seems to filter when `filterOptions` is false and doesn't filter when it's true. Additionally, the empty state detection appears to be checking against the unfiltered data instead of the filtered results, causing incorrect empty state behavior.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

const data = ['Apple', 'Banana', 'Orange'];

function Demo() {
  return (
    <Combobox>
      <Combobox.Target>
        <TextInput />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Options filterOptions={true}>
          {data.map((item) => (
            <Combobox.Option key={item} value={item}>
              {item}
            </Combobox.Option>
          ))}
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

Steps to reproduce:
1. Create a Combobox with `filterOptions={true}`
2. Type a search query in the input
3. Notice that the options are NOT filtered (expected: should be filtered)
4. Set `filterOptions={false}` 
5. Type a search query
6. Notice that the options ARE filtered (unexpected behavior)

Also, when all options are filtered out, the empty state doesn't show up correctly because it's checking the original data array instead of the filtered results.

### Expected behavior

- When `filterOptions={true}`, the options should be filtered based on the search input
- When `filterOptions={false}`, the options should NOT be filtered
- The empty state should appear when the filtered results are empty, not when the original data is empty

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
