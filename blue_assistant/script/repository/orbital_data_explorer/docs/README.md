# orbital-data-explorer

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.

```yaml
script:
  vars:
    seed_urls:
      - https://ode.rsl.wustl.edu/
      - https://oderest.rsl.wustl.edu/
      - https://pds-geosciences.wustl.edu/dataserv/default.htm
      - https://github.com/samiriff/mars-ode-data-access

  nodes:
    researching_the_questions:
      action: generic
      prompt: >
        We want to access Orbital Data Explorer, ODE for short, using STAC conventions. So, we consider ODE as a catalog and 
        call each separate dataset in ODE as a collection. Read the following text and write a python function that generates 
        the list of collections in ODE relevant to Mars, Moon, Venus, or Mercury.

        Then, write a python function that finds an item in one of the listed datasets. :::input
      max_iterations: 20
    integration_api_one:
      action: generic
    integration_api_two:
      action: generic

```
[metadata.yaml](../metadata.yaml)

🔥

```bash
@select orbital-data-explorer-$(@@timestamp)
@assistant script run - \
    script=orbital_data_explorer .

@assets publish push .
```


🔥

---

- [round 1](./round-1.md)
