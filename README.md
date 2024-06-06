# IR Lab SoSe 2024 at Augsburg/Jena/Köln/Leipzig

See [https://tira-io.github.io/ir-lab-sose-24/](https://tira-io.github.io/ir-lab-sose-24/) for details.

Some examples:

TBD

Components:

- [Indexing Backend](construct_indices) (test coverage: ![test coverage backend](construct_indices/coverage.svg))
- [UI](ui) (test coverage: ![Coverage of the frontend](ui/coverage/badge-lines.svg))

## Update the datasets

Add new datasets via:

```
./construct_indices/remote_indexes.py
```

```
./construct_indices/construct_topics_for_ui.py
```

```
./ir-components-archive/create_ir_components_archive.py
```

## Setup Your Development Environment

We use [devcontainers](https://code.visualstudio.com/docs/devcontainers/containers) for development. To start your environment, either use Github Codespaces (click on "Code" -> "Codespaces" in Github to open one) as the easiest way to get started or [devpod](https://github.com/loft-sh/devpod) as open source alternative (directly pointing to our Kubernetes or your local docker installation).

