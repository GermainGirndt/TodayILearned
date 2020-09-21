# Smooth Scrow Using Ref

### Set-up

```
import React, { useRef } from "react";

const formRef = useRef(null);

const handleScrollToRef = (ref) =>
  ref.current.scrollIntoView({
    behavior: "smooth",
    block: "start",
  });
  
```


### Placing Ref into Element

```
<div ref={formRef}>
  <input type=text/>
</div>            
```


### Executing Function

```
<button
  onClick={() => handleScrollToRef(formRef)}
>
  BUTTON MESSAGE
</button>
```
