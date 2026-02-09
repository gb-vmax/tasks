# Bug Report

### Describe the bug

When using `Switch` component within a `Switch.Group`, the onChange handler is not receiving the event object properly. The event parameter appears to be undefined when the context's onChange is called.

### Reproduction

```jsx
import { Switch } from '@mantine/core';

function App() {
  const [values, setValues] = useState([]);
  
  return (
    <Switch.Group value={values} onChange={setValues}>
      <Switch 
        value="option1" 
        label="Option 1"
        onChange={(event) => {
          console.log(event.target.checked); // Should log boolean value
          console.log(event.target.value); // Should log "option1"
        }}
      />
    </Switch.Group>
  );
}
```

### Expected behavior

The onChange handler should receive the full event object with `target.checked` and `target.value` properties accessible. The context's onChange should be called with the event so it can properly update the group's state.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
