# Bug Report

### Describe the bug

After a recent update, the Combobox component is throwing a syntax error and failing to render. It appears there's a malformed export statement in the `ComboboxClearButton` component that's breaking the entire component.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function Demo() {
  return (
    <Combobox>
      <Combobox.Target>
        <input />
      </Combobox.Target>
      <Combobox.Dropdown>
        <Combobox.Options>
          <Combobox.Option value="test">Test</Combobox.Option>
        </Combobox.Options>
      </Combobox.Dropdown>
    </Combobox>
  );
}
```

### Expected behavior

The Combobox should render without any errors. Instead, I'm getting a syntax error when trying to use any Combobox component, even basic usage like the example above.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

The component was working fine before the latest update. It looks like there might be some issue with how the ComboboxClearButton is being exported or defined.

---
Repository: /testbed
