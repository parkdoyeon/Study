defmodule TextClient.Interact do

  @hangman_server :"hangman@kakao-entui-MacBookPro"
  alias TextClient.{ State, Player }

  def start() do
    new_game()
    |> setup_state()
    |> Player.play()
    |> IO.inspect
  end

  defp new_game() do
    :rpc.call(@hangman_server, Hangman, :new_game, []) #얼랭의 rpc라이브러리는 다른 연결된 노드의 함수를 실행하게한다
  end

  defp setup_state(game) do
    %State{
      game_service: game,
      tally: Hangman.tally(game),
    }
  end

  def play(state) do
    # interact
    play(state)
  end

end
