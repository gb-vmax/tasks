# Bug Report

### Describe the bug

I'm experiencing an issue with the Combobox component where passing `null` as data causes a crash instead of being handled gracefully. The component used to return an empty array when data was falsy, but now it seems to return `null` which breaks things downstream.

### Reproduction

```tsx
import { Combobox } from '@mantine/core';

function MyComponent() {
  const [data, setData] = useState(null);
  
  // This causes an error
  return (
    <Combobox>
      <Combobox.Options>
        {data && data.map(item => (
          <Combobox.Option key={item.value} value={item.value}>
            {item.label}
          </Combobox.Option>
        ))}
      </Combobox.Options>
    </Combobox>
  );
}
```

When `data` is `null` or `undefined`, I'm getting errors because the component seems to be returning `null` instead of an empty array. This breaks any code that expects an array to be returned.

### Expected behavior

When `data` is `null` or `undefined`, the function should return an empty array `[]` so that downstream code can safely call array methods like `.map()` without additional null checks.

### System Info

- @mantine/core version: latest
- React version: 18.x
- Browser: Chrome

---
Repository: /testbed
