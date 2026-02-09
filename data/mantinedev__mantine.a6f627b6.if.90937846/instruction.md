# Bug Report

### Describe the bug

When passing `undefined` or `null` data to Combobox components, I'm getting a runtime error instead of an empty dropdown. The application crashes with "Cannot read properties of null" or similar errors.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function MyComponent() {
  const [data, setData] = useState(undefined);
  
  return (
    <Combobox data={data}>
      {/* ... */}
    </Combobox>
  );
}
```

When `data` is `undefined` or `null`, the component should render an empty dropdown, but instead it throws an error and breaks the entire component tree.

### Expected behavior

The Combobox should handle `undefined` or `null` data gracefully and render an empty dropdown without throwing errors. This worked in previous versions where passing undefined data would just show no options.

### System Info
- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome 120

---
Repository: /testbed
