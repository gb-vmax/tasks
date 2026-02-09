# Bug Report

### Describe the bug

The `useHovered` hook is initializing the hovered state with `null` instead of `-1`, which breaks components that rely on the initial state being `-1` to indicate no item is hovered.

### Reproduction

```jsx
import { useHovered } from '@mantine/core';

function MyComponent() {
  const [hovered, { setHovered, resetHovered }] = useHovered();
  
  // This now returns null instead of -1
  console.log(hovered); // Expected: -1, Actual: null
  
  // Components checking for hovered === -1 will break
  const isNothingHovered = hovered === -1; // Always false now
  
  return (
    <div>
      {items.map((item, index) => (
        <div 
          key={index}
          onMouseEnter={() => setHovered(index)}
          onMouseLeave={resetHovered}
          style={{ 
            // This condition no longer works as expected
            background: hovered === -1 ? 'white' : hovered === index ? 'blue' : 'gray'
          }}
        >
          {item}
        </div>
      ))}
    </div>
  );
}
```

### Expected behavior

The initial hovered state should be `-1` to maintain backward compatibility. Components that check `hovered === -1` to determine if nothing is hovered should continue to work.

### System Info

- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
