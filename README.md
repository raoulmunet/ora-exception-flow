# ora-exception-flow

[![tests](https://github.com/raoulmunet/ora-exception-flow/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-exception-flow/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Visualize the exception-handling paths of Oracle PL/SQL blocks.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported for common PL/SQL exception syntax |
> | Oracle Database 23ai | ✅ Supported for common PL/SQL exception syntax |
> | Oracle AI Database 26ai | ✅ Supported for common PL/SQL exception syntax |
>
> The tool is an offline static visualizer. It does not execute PL/SQL and cannot know which exception will occur at runtime.

## Features

- detects `EXCEPTION` sections;
- detects `WHEN ... THEN` handlers;
- distinguishes explicit `RAISE;` propagation from handled/consumed paths;
- generates text, JSON and Mermaid;
- useful for code review and teaching error propagation.

## Usage

```bash
ora-exception-flow examples/load_customer.sql
ora-exception-flow examples/load_customer.sql --format mermaid
```

Example result:

```text
NO_DATA_FOUND -> handler -> RAISE
DUP_VAL_ON_INDEX -> handler -> handled
OTHERS -> handler -> RAISE
```

## Important limitation

Static analysis cannot determine whether a handler actually runs. Nested blocks and exception names built around application-specific conventions are parsed conservatively.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
