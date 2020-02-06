defmodule Hangman do

  # API는 Top Level에서 모든 요청을 전달한다
  # API는 구현체와 분리하는 것이 좋다. defdelegate는 구현체와 API를 나이스하게 분리하는 방법이다.

  def new_game() do
    #Hangman.Server.start_link()
    {:ok, pid } = Supervisor.start_child(Hangman.Supervisor, [])
    pid
  end

  def tally(game_pid) do
    GenServer.call(game_pid, {:tally})
  end

  def make_move(game_pid, guess) do
    GenServer.call(game_pid, {:make_move, guess})
  end

  # alias Hangman.Game #마지막 네임스페이스인 Game만 작성해도 인식.

  #defdelegate new_game(),             to: Game #alias를 지정해주고 Game으로 넘기면 new_game() API가 내부로 연결된다
  #defdelegate tally(game),            to: Game
  #defdelegate make_move(game, guess), to: Game

end
