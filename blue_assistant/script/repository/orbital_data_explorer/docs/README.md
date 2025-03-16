# orbital-data-explorer 🔥

Access to the [Orbital Data Explorer](https://ode.rsl.wustl.edu/).

🔥

```yaml
script:
  vars:
    context_prompt: |
      Our objective is to access the Orbital Data Explorer, ODE for short, using STAC 
      terminology. For this purpose, we consider ODE as a catalog and each separate dataset 
      in ODE as a collection that contains items. We call these items objects or datacubes.

    research_prompt: |
      Read the following text and extract information relevant to this objective.

    research_seed_urls:
      - https://ode.rsl.wustl.edu/
      - https://oderest.rsl.wustl.edu/
      - https://pds-geosciences.wustl.edu/dataserv/default.htm
      - https://github.com/samiriff/mars-ode-data-access

    summarize_prompt: |
      Summarize the following.

  nodes:
    researching_the_questions:
      runnable: true
      action: web_crawl
      prompt: >
        :::context_prompt
        :::research_prompt
      max_iterations: 100
      seed_urls: :::research_seed_urls
      test_mode:
        max_iterations: 1

    summarize_research:
      runnable: false
      action: generate_text
      prompt: >
        :::context_prompt
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

@publish tar .
```



<details>
<summary>metadata</summary>

```yaml
crawl_cache:
  https://github.com/samiriff/mars-ode-data-access: text/html; charset=utf-8
  https://github.com/samiriff/mars-ode-data-access#start-of-content: text/html; charset=utf-8
  https://ode.rsl.wustl.edu/: text/html
  https://ode.rsl.wustl.edu/mars/index.aspx: text/html; charset=utf-8
  https://ode.rsl.wustl.edu/mercury/index.aspx: text/html; charset=utf-8
  https://ode.rsl.wustl.edu/moon/index.aspx: text/html; charset=utf-8
  https://ode.rsl.wustl.edu/venus/index.aspx: text/html; charset=utf-8
  https://oderest.rsl.wustl.edu/: text/html
  https://oderest.rsl.wustl.edu/#GDSRESTInterface: text/html
  https://oderest.rsl.wustl.edu/#ODERESTInterface: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/GDSDLRERDR.html: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/GDSLOLARDR.html: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/GDSMLARDR.html: text/html
  https://oderest.rsl.wustl.edu/GDSWeb/GDSMOLAPEDR.html: text/html
  https://oderest.rsl.wustl.edu/GDS_REST_V2.0.pdf: application/pdf
  https://oderest.rsl.wustl.edu/LPSC42_ODE.pdf: application/pdf
  https://oderest.rsl.wustl.edu/LPSC45_ODE_Abstract.pdf: application/pdf
  https://oderest.rsl.wustl.edu/LPSC45_ODE_Poster.pdf: application/pdf
  https://oderest.rsl.wustl.edu/ODE_REST_V2.1.6.pdf: application/pdf
  https://oderest.rsl.wustl.edu/gdsweb/GDSDLRERDR.html: text/html
  https://oderest.rsl.wustl.edu/gdsweb/GDSLOLARDR.html: text/html
  https://oderest.rsl.wustl.edu/gdsweb/GDSMLARDR.html: text/html
  https://oderest.rsl.wustl.edu/gdsweb/GDSMOLAPEDR.html: text/html
  https://oderest.rsl.wustl.edu/live2/?query=featureclasses&odemetadb=mars: text/xml;
    charset=utf-8
  https://oderest.rsl.wustl.edu/live2/?query=featurenames&odemetadb=mars: text/xml;
    charset=utf-8
  https://oderest.rsl.wustl.edu/live2/?query=iipt: text/xml; charset=utf-8
  ? https://oderest.rsl.wustl.edu/live2?query=products&target=mars&results=c&ihid=MRO&iid=HiRISE&pt=RDRV11&minlat=0.0&maxlat=10.0&westernlon=1&easternlon=5&loc=b
  : text/xml; charset=utf-8
  https://oderest.rsl.wustl.edu/live2?target=mars&query=product&results=c&output=XML&pt=RDR&iid=HiRISE&ihid=MRO: text/xml;
    charset=utf-8
  https://oderest.rsl.wustl.edu/live2?target=mars&query=product&results=cm&output=XML&pt=RDR&iid=HiRISE&ihid=MRO: text/xml;
    charset=utf-8
  ? https://oderest.rsl.wustl.edu/livegds?query=divinerrdr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01&channel=tffffffff
  : unknown
  https://oderest.rsl.wustl.edu/livegds?query=lolardr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01: unknown
  https://oderest.rsl.wustl.edu/livegds?query=molapedr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01: unknown
  https://pds-geosciences.wustl.edu/dataserv/default.htm: text/html
crawl_queue: []
output:
  script:
    nodes:
      researching_the_questions:
        action: web_crawl
        completed: true
        max_iterations: 100
        output: TBA
        prompt: ':::context_prompt :::research_prompt

          '
        runnable: true
        seed_urls: :::research_seed_urls
        test_mode:
          max_iterations: 1
        visited_urls:
          https://github.com/samiriff/mars-ode-data-access: text/html; charset=utf-8
          https://github.com/samiriff/mars-ode-data-access#start-of-content: text/html;
            charset=utf-8
          https://ode.rsl.wustl.edu/: text/html
          https://ode.rsl.wustl.edu/mars/index.aspx: text/html; charset=utf-8
          https://ode.rsl.wustl.edu/mercury/index.aspx: text/html; charset=utf-8
          https://ode.rsl.wustl.edu/moon/index.aspx: text/html; charset=utf-8
          https://ode.rsl.wustl.edu/venus/index.aspx: text/html; charset=utf-8
          https://oderest.rsl.wustl.edu/: text/html
          https://oderest.rsl.wustl.edu/#GDSRESTInterface: text/html
          https://oderest.rsl.wustl.edu/#ODERESTInterface: text/html
          https://oderest.rsl.wustl.edu/GDSWeb/: text/html
          https://oderest.rsl.wustl.edu/GDSWeb/GDSDLRERDR.html: text/html
          https://oderest.rsl.wustl.edu/GDSWeb/GDSLOLARDR.html: text/html
          https://oderest.rsl.wustl.edu/GDSWeb/GDSMLARDR.html: text/html
          https://oderest.rsl.wustl.edu/GDSWeb/GDSMOLAPEDR.html: text/html
          https://oderest.rsl.wustl.edu/GDS_REST_V2.0.pdf: application/pdf
          https://oderest.rsl.wustl.edu/LPSC42_ODE.pdf: application/pdf
          https://oderest.rsl.wustl.edu/LPSC45_ODE_Abstract.pdf: application/pdf
          https://oderest.rsl.wustl.edu/LPSC45_ODE_Poster.pdf: application/pdf
          https://oderest.rsl.wustl.edu/ODE_REST_V2.1.6.pdf: application/pdf
          https://oderest.rsl.wustl.edu/gdsweb/GDSDLRERDR.html: text/html
          https://oderest.rsl.wustl.edu/gdsweb/GDSLOLARDR.html: text/html
          https://oderest.rsl.wustl.edu/gdsweb/GDSMLARDR.html: text/html
          https://oderest.rsl.wustl.edu/gdsweb/GDSMOLAPEDR.html: text/html
          https://oderest.rsl.wustl.edu/live2/?query=featureclasses&odemetadb=mars: text/xml;
            charset=utf-8
          https://oderest.rsl.wustl.edu/live2/?query=featurenames&odemetadb=mars: text/xml;
            charset=utf-8
          https://oderest.rsl.wustl.edu/live2/?query=iipt: text/xml; charset=utf-8
          ? https://oderest.rsl.wustl.edu/live2?query=products&target=mars&results=c&ihid=MRO&iid=HiRISE&pt=RDRV11&minlat=0.0&maxlat=10.0&westernlon=1&easternlon=5&loc=b
          : text/xml; charset=utf-8
          https://oderest.rsl.wustl.edu/live2?target=mars&query=product&results=c&output=XML&pt=RDR&iid=HiRISE&ihid=MRO: text/xml;
            charset=utf-8
          https://oderest.rsl.wustl.edu/live2?target=mars&query=product&results=cm&output=XML&pt=RDR&iid=HiRISE&ihid=MRO: text/xml;
            charset=utf-8
          ? https://oderest.rsl.wustl.edu/livegds?query=divinerrdr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01&channel=tffffffff
          : unknown
          https://oderest.rsl.wustl.edu/livegds?query=lolardr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01: unknown
          https://oderest.rsl.wustl.edu/livegds?query=molapedr&results=vsi&maxlat=0.01&minlat=0.0&westernlon=0.0&easternlon=0.01: unknown
          https://pds-geosciences.wustl.edu/dataserv/default.htm: text/html
      summarize_research:
        action: generate_text
        completed: true
        depends-on: researching_the_questions
        prompt: ':::context_prompt :::summarize_prompt

          '
        runnable: false
      writing_code:
        action: generate_text
        completed: true
        depends-on: summarize_research
        runnable: false
    vars:
      context_prompt: "Our objective is to access the Orbital Data Explorer, ODE for\
        \ short, using STAC \nterminology. For this purpose, we consider ODE as a\
        \ catalog and each separate dataset \nin ODE as a collection that contains\
        \ items. We call these items objects or datacubes.\n"
      research_prompt: 'Read the following text and extract information relevant to
        this objective.

        '
      research_seed_urls:
      - https://ode.rsl.wustl.edu/
      - https://oderest.rsl.wustl.edu/
      - https://pds-geosciences.wustl.edu/dataserv/default.htm
      - https://github.com/samiriff/mars-ode-data-access
      summarize_prompt: 'Summarize the following.

        '
script:
  nodes:
    researching_the_questions:
      action: web_crawl
      max_iterations: 100
      prompt: ':::context_prompt :::research_prompt

        '
      runnable: true
      seed_urls: :::research_seed_urls
      test_mode:
        max_iterations: 1
    summarize_research:
      action: generate_text
      depends-on: researching_the_questions
      prompt: ':::context_prompt :::summarize_prompt

        '
      runnable: false
    writing_code:
      action: generate_text
      depends-on: summarize_research
      runnable: false
  vars:
    context_prompt: "Our objective is to access the Orbital Data Explorer, ODE for\
      \ short, using STAC \nterminology. For this purpose, we consider ODE as a catalog\
      \ and each separate dataset \nin ODE as a collection that contains items. We\
      \ call these items objects or datacubes.\n"
    research_prompt: 'Read the following text and extract information relevant to
      this objective.

      '
    research_seed_urls:
    - https://ode.rsl.wustl.edu/
    - https://oderest.rsl.wustl.edu/
    - https://pds-geosciences.wustl.edu/dataserv/default.htm
    - https://github.com/samiriff/mars-ode-data-access
    summarize_prompt: 'Summarize the following.

      '

```

</details>


[orbital-data-explorer-2025-03-15-sxjbbf](https://kamangir-public.s3.ca-central-1.amazonaws.com/orbital-data-explorer-2025-03-15-sxjbbf.tar.gz)

🔥

---

- [round 1](./round-1.md)
