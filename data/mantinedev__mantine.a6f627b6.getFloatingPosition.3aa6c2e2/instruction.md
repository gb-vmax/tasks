# Bug Report

### Describe the bug

When using floating elements with RTL (right-to-left) direction, the positioning is not working correctly. The floating element appears in the wrong position - it seems like the position is being flipped when it shouldn't be, or not being flipped when it should be.

### Reproduction

```js
import { getFloatingPosition } from '@mantine/core';

// RTL direction with right-positioned element
const position1 = getFloatingPosition('rtl', 'right');
console.log(position1); // Expected: 'left', but gets 'right'

// RTL direction with left-positioned element  
const position2 = getFloatingPosition('rtl', 'left');
console.log(position2); // Expected: 'right', but gets 'left'

// RTL with placement
const position3 = getFloatingPosition('rtl', 'right-start');
console.log(position3); // Expected: 'left-start', but gets something else
```

### Expected behavior

In RTL mode, floating positions with 'left' and 'right' should be mirrored:
- 'right' should become 'left'
- 'left' should become 'right'  
- 'right-start' should become 'left-start'
- etc.

In LTR mode, positions should remain unchanged.

### System Info

- @mantine/core version: latest
- Browser: All browsers affected

---
Repository: /testbed
