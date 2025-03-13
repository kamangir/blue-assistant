# Hue 🔥

```yaml
script:
  vars:
    objective: Write Python + Bash code to send a color command to the Hue LED lights in my apartment.
  nodes:
    generating_the_code:
      action: generate_text
      prompt: :::objective

```
[metadata.yaml](../metadata.yaml)

🔥

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue . \
  --verbose 1
```


```yaml
{}

```

---

- [round 1](./README-round-1.md)
