# Bug Report

### Describe the bug

The `camelToKebabCase` utility function is not converting camelCase strings to kebab-case format correctly. Instead of converting to kebab-case (with hyphens), it's producing output with underscores, and it's also replacing ALL letters instead of just uppercase ones.

### Reproduction

```js
import { camelToKebabCase } from '@mantine/core';

// Expected: "background-color"
// Actual: "_b_a_c_k_g_r_o_u_n_d_c_o_l_o_r"
console.log(camelToKebabCase('backgroundColor'));

// Expected: "my-component-name"
// Actual: "_m_y_c_o_m_p_o_n_e_n_t_n_a_m_e"
console.log(camelToKebabCase('myComponentName'));

// Expected: "font-size"
// Actual: "_f_o_n_t_s_i_z_e"
console.log(camelToKebabCase('fontSize'));
```

### Expected behavior

The function should convert camelCase strings to kebab-case by:
1. Inserting a hyphen before each uppercase letter
2. Converting the uppercase letter to lowercase
3. Not affecting lowercase letters

For example:
- `backgroundColor` → `background-color`
- `myComponentName` → `my-component-name`
- `fontSize` → `font-size`

### System Info

- @mantine/core version: latest
- This appears to be affecting CSS property conversions and style prop handling

---
Repository: /testbed
