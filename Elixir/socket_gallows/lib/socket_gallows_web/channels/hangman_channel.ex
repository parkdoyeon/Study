defmodule SocketGallows.Web.HangmanChannel do
  use Phoenix.Channel

  #socket은 conn과 같이 상태를 관리한다.
  def join("hangman: game", _, socket) do
    { :ok, socket }
  end
end
