defmodule Hangman.Server do

  # 제너릭서버로, 얼랭 OTP 프레임워크의 핵심적인 요소이다.
  # 외부 API로 Start, Invoke, Monitor, Stop를 제공하고
  # 내부 API로 콜백을 다루는 Initialize, Handle Requests, Handle Events를 다룬다.
  # 외부 API는 콜링 프로세스에 관여하고 내부 API는 서버 프로세스에 관여한다.

  alias Hangman.Game
  use GenServer

  def start_link() do
    GenServer.start_link(__MODULE__, nil)
  end

  def init(_) do
    { :ok, Game.new_game() }
  end

  def handle_call({:make_move, guess}, _from, game) do
    { game, tally } = Game.make_move(game, guess)
    { :reply, tally, game }
  end

  def handle_call({:tally}, _from, game) do
    { :reply, Game.tally(game), game }
  end
end
