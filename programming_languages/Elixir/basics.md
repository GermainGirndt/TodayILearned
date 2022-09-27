# Elixir

- Compiled languages (to Erlang)
- Mature and scalable languages
- Erlang was communication focused

## Install

https://elixir-lang.org/install.html

## Install phoenix

`mix archive.install hex phx_new 1.5.7`

## Project Start (Generic)

`mix phx.new PROJECT_NAME`

## Project Start (API)

`mix phx.new PROJECT_NAME--no-webpack --no-html`

## DB

```
mix ecto.setup
mix ecto.create
mix ecto.gen.migration MIGRATION_NAME
mix ecto.migrate

mix ecto.drop #drops DB
```

## Install credo - syntatical analyzer

In `mix.exs` (package manager) add following dependency:
`{:credo, "~> 1.5", only: [:dev, :test], runtime: false}`

Install - Terminal
`mix deps.get`

Config
`mix credo gen.config`

Change:
`{Credo.Check.Readability.ModuleDoc, []},`
To:
`{Credo.Check.Readability.ModuleDoc, false},`

(For now, we don't want any documentation

### Execute server

`mix phx.server`

Access
`http://localhost:4000/dashboard/home`
