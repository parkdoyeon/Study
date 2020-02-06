# mix new hangman --sup 명령어를 통해 프로젝트를 생성하면 자동으로 supervisor가 붙은 프로젝트가 생성된다.
defmodule Hangman.Application do

  use Application

  def start(_type, _args) do
    import Supervisor.Spec, warn: false

    children = [
      worker(Hangman.Server, []),
    ]

    options = [
      name: Hangman.Supervisor,
      strategy: :simple_one_for_one #
    ]

    Supervisor.start_link(children, options)
  end
end
