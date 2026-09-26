# ora-exception-flow

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

## License

MIT.
