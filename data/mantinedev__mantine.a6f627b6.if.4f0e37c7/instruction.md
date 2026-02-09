# Bug Report

### Describe the bug

When using charts without providing a `series` prop, the application crashes with a TypeError. This seems to be a regression as it was working fine before.

### Reproduction

```jsx
import { LineChart } from '@mantine/charts';

function MyChart() {
  return (
    <LineChart
      data={[
        { date: '2024-01', value: 100 },
        { date: '2024-02', value: 200 },
      ]}
      // series prop is undefined/not provided
    />
  );
}
```

### Expected behavior

The chart should handle undefined series gracefully and either render with default settings or show an empty chart without throwing errors.

### Error message

```
TypeError: Cannot read properties of null (reading 'reduce')
```

or similar errors when trying to iterate over the series labels.

### System Info

- @mantine/charts version: latest
- React version: 18.x
- Browser: Chrome/Firefox

---
Repository: /testbed
