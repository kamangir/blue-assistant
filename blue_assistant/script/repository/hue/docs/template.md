# Hue

```yaml
include:::noref ../metadata.yaml
```
[metadata.yaml](../metadata.yaml)

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue .

@assets publish \
  extensions=png,push .
```
set:::object_name hue-2025-03-14-hpow92

---

```bash
@hue create_user
```

```bash
@hue list
```

```text
🧠  found 16 light(s): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
```

```bash
@hue test
```

details:::output
metadata:::get:::object_name:::output
details:::

| | |
|-|-|
| assets:::get:::object_name/thumbnail-workflow.png | assets:::blue-assistant/20250314_143702.jpg |

---

- [round 1](./round-1.md)