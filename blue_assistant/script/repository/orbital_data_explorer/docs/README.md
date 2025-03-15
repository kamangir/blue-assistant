# orbital-data-explorer 🔥

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/), through AI.

🔥

```yaml
script:
  vars:
    overview_prompt: |
      We want to access Orbital Data Explorer, ODE for short, using STAC terminology. So, we consider ODE as a catalog and 
      call each separate dataset in ODE as a collection that contains items. We call these items objects or datacubes.
    research_prompt: |
      Read the following text and extract the relevant information.
    research_seed_urls:
      - https://ode.rsl.wustl.edu/
      - https://oderest.rsl.wustl.edu/
      - https://pds-geosciences.wustl.edu/dataserv/default.htm
      - https://github.com/samiriff/mars-ode-data-access
    summarize_prompt: |
      Summarize the following.

  nodes:
    researching_the_questions:
      runnable: false
      action: generic
      prompt: |
        :::overview_prompt
        :::research_prompt
      max_iterations: 20

    summarize_research:
      runnable: false
      action: generate_text
      prompt: |
        :::overview_prompt
        :::summarize_prompt
      depends-on: researching_the_questions

    writing_code:
      runnable: false
      action: generate_text
      depends-on: summarize_research

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
