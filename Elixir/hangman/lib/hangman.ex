defmodule Hangman do
  def hello do
    IO.puts Dictionary.random_word()
  end

  # API는 구현체와 분리하는 것이 좋다. defdelegate는 구현체와 API를 나이스하게 분리하는 방법이다.
  alias Hangman.Game #마지막 네임스페이스인 Game만 작성해도 인식.

  defdelegate new_game(),             to: Game #alias를 지정해주고 Game으로 넘기면 new_game() API가 내부로 연결된다
  defdelegate tally(game),            to: Game

  def make_move(game, guess) do
    game = Game.make_move(game, guess)
    { game, tally(game) }
  end
end
