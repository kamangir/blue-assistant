# Hue

## output

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

![image](https://github.com/kamangir/assets/blob/main/blue-assistant/20250314_143702.jpg?raw=true)

## script

```yaml
script:
  vars:
    set_light_color_prompt: |
      Complete this Python function to send a color command to a Hue light.
    set_light_color_signature: |
      def set_light_color(
          bridge_ip: str,
          username: str,
          light_id: str,
          hue: int,  # 0 to 65535
          saturation: int,  # 0 to 254
          verbose: bool = False,
      ) -> bool:
          logger.info(
              "{}.set_light_color({}@{}:{}) -> hue=0x{:x}, saturation=0x{:x}".format(
                  NAME,
                  username,
                  bridge_ip,
                  light_id,
                  hue,
                  saturation,
              )
          )

          ...

          return True
    bridge_ip_prompt: |
      Generate instructions for finding my Hue bridge IP address.
    create_user_prompt: |
      Write Python code to create a developer username on my Philips Hue Bridge.
    list_lights_prompt: |
      Write Python code to list the lights available on my Philips Hue Bridge.

  nodes:
    generating_set_light_color:
      completed: true
      action: generate_text
      prompt: |
        :::set_light_color_prompt

        :::set_light_color_signature
    acquiring_bridge_ip:
      completed: true
      action: generate_text
      prompt: :::bridge_ip_prompt
    generating_create_user:
      completed: true
      action: generate_text
      prompt: :::create_user_prompt
      depends-on: acquiring_bridge_ip
    list_lights:
      completed: true
      action: generate_text
      prompt: :::list_lights_prompt
      depends-on: generating_create_user

```
[metadata.yaml](../metadata.yaml)

```bash
@select hue-$(@@timestamp)

@assistant script run - \
  script=hue .

@assets publish \
	extensions=png,push .
```


![image](https://github.com/kamangir/assets/blob/main/hue-2025-03-14-hpow92/thumbnail-workflow.png?raw=true)

---

- [round 1](./round-1.md)
