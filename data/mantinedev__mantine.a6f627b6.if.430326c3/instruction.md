# Bug Report

### Describe the bug

Getting a runtime error when using Combobox with an empty array as data. The component throws a "Cannot read properties of null" error when trying to render with `data={[]}`.

### Reproduction

```jsx
import { Combobox } from '@mantine/core';

function MyComponent() {
  const [data, setData] = useState([]);
  
  return (
    <Combobox data={data}>
      {/* Component content */}
    </Combobox>
  );
}
```

When the `data` prop is set to an empty array `[]`, the component crashes instead of rendering an empty state.

### Expected behavior

The Combobox should handle empty arrays gracefully and render without errors, similar to how it handles `undefined` or `null` values.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
