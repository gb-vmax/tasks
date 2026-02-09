# Bug Report

### Describe the bug
When using Radio components within a Radio.Group, the group's `onChange` handler is not being called when an individual radio button is selected if the radio has its own `onChange` handler defined.

### Reproduction
```jsx
import { Radio } from '@mantine/core';

function App() {
  const [value, setValue] = useState('');

  return (
    <Radio.Group 
      value={value} 
      onChange={(val) => {
        console.log('Group onChange called:', val); // This doesn't get called
        setValue(val);
      }}
    >
      <Radio 
        value="option1" 
        label="Option 1"
        onChange={(e) => console.log('Radio onChange called')} 
      />
      <Radio 
        value="option2" 
        label="Option 2"
        onChange={(e) => console.log('Radio onChange called')} 
      />
    </Radio.Group>
  );
}
```

### Expected behavior
Both the individual Radio's `onChange` and the Radio.Group's `onChange` should be called when a radio button is selected. The group's state should update properly even when individual radios have their own change handlers.

Currently, when a Radio has its own `onChange` prop, the group's `onChange` is not triggered, breaking the expected behavior of the Radio.Group component.

### System Info
- @mantine/core version: latest
- React version: 18.x

---
Repository: /testbed
