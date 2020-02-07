defmodule TextClient.MixProject do
  use Mix.Project

  def project do
    [
      app: :text_client,
      version: "0.1.0",
      elixir: "~> 1.9",
      start_permanent: Mix.env() == :prod,
      deps: deps()
    ]
  end

  # Run "mix help compile.app" to learn about applications.
  def application do
    [
      #hangman을 코드에 포함시키되 실행하지는 않는다. 이 옵션이 빠지면 자동으로 Hangman서버가 시작된다.
      included_applications: [ :hangman ],
      extra_applications: [:logger]
    ]
  end

  # Run "mix help deps" to learn about dependencies.
  defp deps do
    [
      { :hangman, [ path: "../hangman" ] },
    ]
  end
end
