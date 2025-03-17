# @web

A minimal web interface for an [AI](https://github.com/kamangir/openai-commands) agent.

## @web fetch

```bash
@web fetch - https://ode.rsl.wustl.edu/ -
```

set:::fetch_object_name web-fetch-2025-03-14-jket7u

details:::metadata
metadata:::get:::fetch_object_name
details:::

## @web crawl

```bash
@select crawl-$(@@timestamp)

@web crawl cache \
    https://ode.rsl.wustl.edu/+https://oderest.rsl.wustl.edu/ . \
    --max_iterations 20

@publish tar .
```

set:::crawl_object_name crawl-2025-03-15-s8jrfg

details:::metadata
metadata:::get:::crawl_object_name
details:::

object:::get:::crawl_object_name